from flask import Flask, render_template_string, request, session, redirect, url_for, Blueprint
import os

favorites_blueprint = Blueprint('favorites_blueprint', __name__)

app = Flask(__name__)
app.secret_key = os.urandom(24) 

@app.route('/')
def index():
    selected_sowars = session.get('selected_sowars', [])
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{{ title }}</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
            body {
                background: url('/static/masjed-img.jpg') no-repeat center center fixed;
                background-size: cover;
                margin: 0;
                max-width: 100%;
                height: auto;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            .container {
                padding: 20px;
                border-radius: 10px;
                margin-top: 50px;
            }

            h1 {
                text-align: center;
                font-family: 'Old Arabic Font', sans-serif;
                font-size: 2em;
                color: #2c3e50;
            }

            .btn {
                font-size: 1.5em;
                border-radius: 10px;
                transition: background-color 0.3s ease, transform 0.2s ease;
            }

            .btn:hover {
                background-color: #2c3e50;
                transform: scale(1.1);
            }

            .selected-sowar-box {
                background-color: #3498db;
                color: #fff;
                padding: 10px;
                border-radius: 5px;
                margin-top: 10px;
                text-align: center;
            }
footer {
    background-color: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

footer p {
    margin: 0;
}

        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="my-5">{{ title }}</h1>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="https://almanar.com.lb/legacy/salat.php" target="_blank" class="btn btn-primary btn-block">مواقيت الصلاة</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="https://forums.alkafeel.net/node/114411" target="_blank" class="btn btn-primary btn-block">الذكر</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="https://surahquran.com/video-qEm1llEPuRs.html" target="_blank" class="btn btn-primary btn-block">الأصوات</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="favorites.html" target="_blank" class="btn btn-primary btn-block">المفضلة</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="https://read.quranexplorer.com/1/1/7/Usmani/Mishari-Rashid/Hide/Tajweed-OFF"target="_blank" class="btn btn-primary btn-block">قوائم التشغيل</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="https://masba7a.com/"target="_blank" class="btn btn-primary btn-block">المسبحة</a>
                </div>
            </div>
        </div>
        <p style="position:fixed;bottom:0;">&#169; COPYRIGHTS 2024 MZ</p>
<footer>
    <div class="container">
        <p>&#169;2024 MM. All rights reserved.</p>
    </div>
</footer>

    </body>
    </html>
    """
    return render_template_string(template, title="حقيبة المؤمن", selected_sowars=selected_sowars)

@favorites_blueprint.route('/favorites.html', methods=['GET', 'POST'])
def favorites():
    if request.method == 'POST':
        selected_sowars = request.form.getlist('sowars')
        session['selected_sowars'] = selected_sowars
        return redirect(url_for('favorites_blueprint.favorites'))

    selected_sowars = session.get('selected_sowars', [])
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>المفضلة</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        <style>
    body {
        background: url('/static/masjed-img.jpg') no-repeat center center fixed;
        background-size: cover;
        margin: 0;
        max-width: 100%;
        height: auto;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .container {
        padding: 20px;
        border-radius: 10px;
        margin-top: 50px;
        display: flex;
        justify-content: center;
    }

    .main-content {
        flex: 1;
        margin-right: 20px;
    }

    .form-check {
        text-align: right;
    }

    .form-check-label {
        direction: rtl;
    }

    .btn {
         font-size: 1.5em;
        border-radius: 10px;
        transition: background-color 0.3s ease, transform 0.2s ease;
        margin-top: 10px;
        width: 600px; /* Set the width of the button */
        height: 60px; /* Set the height of the button */
        display: block;
    }

    .btn:hover {
        background-color: #2c3e50;

    }

    .selected-sowar {
        background-color: #3498db;
        color: #fff;
    }

    .selected-sowar-box {
        background-color: #3498db;
        color: #fff;
        padding: 10px;
        border-radius: 5px;
        margin-top: 10px;
    }
footer {
    background-color: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

footer p {
    margin: 0;
}

</style>
    </head>
    <body>
        <div class="container">
            <div class="main-content">
                <h1 class="my-5">تحديد المفضلة</h1>
                   <form method="post" action="" style="display: flex; flex-wrap: wrap; max-height: 600px; overflow-y: auto;"">
        {% for sowar in [ 
"الفاتحة",
        "البقرة",
        "آل عمران",
        "النساء",
        "المائدة",
        "الأنعام",
        "الأعراف",
        "الأنفال",
        "التوبة",
        "يونس",
        "هود",
        "يوسف",
        "الرعد",
        "إبراهيم",
        "الحجر",
        "النحل",
        "الإسراء",
        "الكهف",
        "مريم",
        "طه",
        "الأنبياء",
        "الحج",
        "المؤمنون",
        "النّور",
        "الفرقان",
        "الشعراء",
        "النمل",
        "القصص",
        "العنكبوت",
        "الرّوم",
        "لقمان",
        "السجدة",
        "الأحزاب",
        "سبإ",
        "فاطر",
        "يس",
        "الصافات",
        "ص",
        "الزمر",
        "غافر",
        "فصّلت",
        "الشورى",
        "الزخرف",
        "الدّخان",
        "الجاثية",
        "الأحقاف",
        "محمد",
        "الفتح",
        "الحجرات",
        "ق",
        "الذاريات",
        "الطور",
        "النجم",
        "القمر",
        "الرحمن",
        "الواقعة",
        "الحديد",
        "المجادلة",
        "الحشر",
        "الممتحنة",
        "الصف",
        "الجمعة",
        "المنافقون",
        "التغابن",
        "الطلاق",
        "التحريم",
        "الملك",
        "القلم",
        "الحاقة",
        "المعارج",
        "نوح",
        "الجن",
        "المزّمّل",
        "المدّثر",
        "القيامة",
        "الإنسان",
        "المرسلات",
        "النبأ",
        "النازعات",
        "عبس",
        "التكوير",
        "الإنفطار",
        "المطفّفين",
        "الإنشقاق",
        "البروج",
        "الطارق",
        "الأعلى",
        "الغاشية",
        "الفجر",
        "البلد",
        "الشمس",
        "الليل",
        "الضحى",
        "الشرح",
        "التين",
        "العلق",
        "القدر",
        "البينة",
        "الزلزلة",
        "العاديات",
        "القارعة",
        "التكاثر",
        "العصر",
        "الهمزة",
        "الفيل",
        "قريش",
        "الماعون",
        "الكوثر",
        "الكافرون",
        "النصر",
        "المسد",
        "الإخلاص",
        "الفلق",
        "الناس" ] %}
        <div class="form-check">
            <input type="checkbox" class="form-check-input" id="{{ loop.index }}" name="sowars" value="{{ sowar }}" {% if sowar in selected_sowars %}checked{% endif %}>
            <label class="form-check-label {% if sowar in selected_sowars %}selected-sowar{% endif %}" for="{{ loop.index }}">{{ sowar }}</label>
        </div>
        {% endfor %}
         <div style="margin-top:50px; margin-left:50px;">
        <button type="submit" class="btn btn-primary mt-3" style="margin-top: px;">حفظ</button>
    </div>
    </form>
            </div>

            <div class="sidebar">
                {% if selected_sowars %}
                <div class="selected-sowar-box">
                    <h2 class="mb-3">المفضلة:</h2>
                    <ul class="list-group">
                        {% for sowar in selected_sowars %}
                        <li class="list-group-item selected-sowar">{{ sowar }}</li>
                        {% endfor %}
                    </ul>
                </div>
                {% endif %}
            </div>
        </div>
        <footer>
    <div class="container">
        <p>&#169;2024 MM. All rights reserved.</p>
    </div>
</footer>
    </body>
    </html>
    """
    return render_template_string(template, selected_sowars=selected_sowars)

app.register_blueprint(favorites_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
