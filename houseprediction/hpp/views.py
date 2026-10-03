from django.shortcuts import render, redirect
from hpp.models import User
import joblib

def home(request):
    return render(request, "home.html")

def signup(request):
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]

        User.objects.create(
            name=name,
            username=username,
            email=email,
            phone=phone,
            password=password
        )

        return redirect("login")

    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.filter(
            username=username,
            password=password
        ).first()

        if user:
            request.session["username"] = user.username
            return redirect("dashboard")

        return render(request, "login.html", {
            "error": "Invalid username or password"
        })

    return render(request, "login.html")

def dashboard(request):
    if "username" not in request.session:
        return redirect("login")

    return render(request, "dashboard.html")

def userlist(request):
    users = User.objects.all()
    return render(request, "userlist.html", {"users": users})

def update_user(request, id):
    user = User.objects.filter(id=id).first()

    if request.method == "POST":
        user.name = request.POST["name"]
        user.username = request.POST["username"]
        user.email = request.POST["email"]
        user.phone = request.POST["phone"]
        user.password = request.POST["password"]
        user.save()

        return redirect("userlist")

    return render(request, "update_user.html", {"user": user})

def delete_user(request, id):
    user = User.objects.filter(id=id).first()
    user.delete()

    return redirect("userlist")

def logout(request):
    request.session.flush()
    return redirect("login")


def predict_price(request):
    if "username" not in request.session:
        return redirect("login")

    if request.method == "POST":
        bedrooms = float(request.POST["bedrooms"])
        bathrooms = float(request.POST["bathrooms"])
        sqft_living = float(request.POST["sqft_living"])
        sqft_lot = float(request.POST["sqft_lot"])
        floors = float(request.POST["floors"])
        waterfront = float(request.POST["waterfront"])
        view = float(request.POST["view"])
        sqft_above = float(request.POST["sqft_above"])
        sqft_basement = float(request.POST["sqft_basement"])
        sqft_living15 = float(request.POST["sqft_living15"])
        sqft_lot15 = float(request.POST["sqft_lot15"])

        model = joblib.load("mlmodel (2).pkl")
        scalers = joblib.load("Scalermodel (2).pkl")

        x_scaler = scalers["x_scaler"]
        y_scaler = scalers["y_scaler"]

        input_data = [[
            bedrooms,
            bathrooms,
            sqft_living,
            sqft_lot,
            floors,
            waterfront,
            view,
            sqft_above,
            sqft_basement,
            sqft_living15,
            sqft_lot15
        ]]

        input_scaled = x_scaler.transform(input_data)

        prediction_scaled = model.predict(input_scaled)

        prediction = y_scaler.inverse_transform(
            prediction_scaled.reshape(-1, 1)
        )

        price = prediction[0][0]

        return render(request, "predictions.html", {
            "price": round(price, 2)
        })

    return render(request, "predictions.html")