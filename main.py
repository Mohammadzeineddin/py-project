from flask import Flask, render_template_string,request, session, redirect, url_for, Blueprint
import os
#define pages and main app
favorites_blueprint = Blueprint('favorites_blueprint', __name__)
mawaket_blueprint = Blueprint('mawaket_blueprint', __name__)
zekr_blueprint = Blueprint('zekr_blueprint', __name__)
aswat_blueprint = Blueprint('aswat_blueprint', __name__)
masb7a_blueprint = Blueprint('masb7a_blueprint', __name__)
app = Flask(__name__)
app.secret_key = os.urandom(24) 
#define main route of homepage
@app.route('/')

def index():
    #homepage html code
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
        </style>
    </head>
    <body>
        <div class="container">
            <h1 class="my-5">{{ title }}</h1>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href=" https://almanar.com.lb/salat.php " class="btn btn-primary btn-block">مواقيت الصلاة</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="zekr.html" class="btn btn-primary btn-block">الذكر</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="aswat.html" class="btn btn-primary btn-block">الأصوات</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="favorites.html" class="btn btn-primary btn-block">المفضلة</a>
                </div>
            </div>
            <div class="row justify-content-center">
                <div class="col-md-4 mb-4">
                    <a href="masb7a.html" class="btn btn-primary btn-block">المسبحة</a>
                </div>
            </div>
        </div>
        <p style="position:fixed;bottom:0;">&#169; COPYRIGHTS 2024 MM</p>
    </body>
    </html>
    """
    #render the homepage template
    return render_template_string(template, title="حقيبة المؤمن")
#favorites route
@favorites_blueprint.route('/favorites.html', methods=['GET', 'POST'])
def favorites():
    #define selected sowars
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
        margin-top:10px;
    }
</style>
    </head>
   <body>
    <div class="container">
        <div class="main-content">
            <h1 class="my-5">تحديد المفضلة</h1>
            <form method="post" action="" style="display: flex; flex-wrap: wrap; max-height: 600px; overflow-y: auto;">
                {% for sowar in [
                    "الفاتحة", "البقرة", "آل عمران", "النساء", "المائدة", "الأنعام", "الأعراف", "الأنفال", "التوبة", "يونس", "هود", "يوسف", "الرعد", "إبراهيم", "الحجر", "النحل", "الإسراء", "الكهف", "مريم", "طه", "الأنبياء", "الحج", "المؤمنون", "النّور", "الفرقان", "الشعراء", "النمل", "القصص", "العنكبوت", "الرّوم", "لقمان", "السجدة", "الأحزاب", "سبإ", "فاطر", "يس", "الصافات", "ص", "الزمر", "غافر", "فصّلت", "الشورى", "الزخرف", "الدّخان", "الجاثية", "الأحقاف", "محمد", "الفتح", "الحجرات", "ق", "الذاريات", "الطور", "النجم", "القمر", "الرحمن", "الواقعة", "الحديد", "المجادلة", "الحشر", "الممتحنة", "الصف", "الجمعة", "المنافقون", "التغابن", "الطلاق", "التحريم", "الملك", "القلم", "الحاقة", "المعارج", "نوح", "الجن", "المزّمّل", "المدّثر", "القيامة", "الإنسان", "المرسلات", "النبأ", "النازعات", "عبس", "التكوير", "الإنفطار", "المطفّفين", "الإنشقاق", "البروج", "الطارق", "الأعلى", "الغاشية", "الفجر", "البلد", "الشمس", "الليل", "الضحى", "الشرح", "التين", "العلق", "القدر", "البينة", "الزلزلة", "العاديات", "القارعة", "التكاثر", "العصر", "الهمزة", "الفيل", "قريش", "الماعون", "الكوثر", "الكافرون", "النصر", "المسد", "الإخلاص", "الفلق", "الناس"
                ] %}
                    <div class="form-check">
                        <input type="checkbox" class="form-check-input" id="{{ loop.index }}" name="sowars" value="{{ sowar }}" {% if sowar in selected_sowars %}checked{% endif%}>
                        <label class="form-check-label {% if sowar in selected_sowars %}selected-sowar{% endif %}" for="{{ loop.index }}">{{ sowar }}</label>
                    </div>
                {% endfor %}
                <div style=" margin-left:50px;">
                    <button type="submit" class="btn btn-primary mt-3" style="width:100px;margin-right:300px;height:50px;" onclick="addToFavorites()">حفظ</button>
                </div>
            </form>
            <table id="favoritesTable" class="table">
                <thead>
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">السورة</th>
                        <th scope="col">حذف</th>
                    </tr>
                </thead>
                <tbody id="favoritesTableBody">
                
                </tbody>
            </table>
        </div>
    </div>
    <!-- Button to return to the homepage -->
    <a href="{{ url_for('index') }}" class="btn btn-primary" style="position: fixed; bottom: 10px; right:20px;width:200px;">الرجوع</a>

    <p style="position:fixed;bottom:0;">&#169; COPYRIGHTS 2024 MMA</p>
</body>
 <script>
        function addToFavorites() {
            const form = document.querySelector("form");
            const favoritesTableBody = document.querySelector("#favoritesTableBody");
            const selectedSowars = new Set();
            
            // Collect all selected suras
            for (const checkbox of form.elements.sowars) {
                if (checkbox.checked) {
                    selectedSowars.add(checkbox.value);
                }
            }
            
            // Remove unchecked suras from the table
            for (const row of favoritesTableBody.querySelectorAll("tr")) {
                const sowar = row.dataset.sowar;
                if (!selectedSowars.has(sowar)) {
                    row.remove();
                    // Uncheck checkbox associated with removed surah
                    const checkbox = document.querySelector(`input[name="sowars"][value="${sowar}"]`);
                    if (checkbox) {
                        checkbox.checked = false;
                    }
                }
            }
            
            // Add new selected suras to the table
            let index = 1;
            for (const sowar of selectedSowars) {
                const existingRow = favoritesTableBody.querySelector(`tr[data-sowar="${sowar}"]`);
                if (!existingRow) {
                    const row = document.createElement("tr");
                    row.dataset.sowar = sowar;
                    row.innerHTML = `
                        <th scope="row">${index}</th>
                        <td>${sowar}</td>
                        <td>
                            <button type="button" class="btn btn-danger" style="width:100px;height:50px;" onclick="deleteRow('${sowar}')">حذف</button>
                        </td>
                    `;
                    favoritesTableBody.appendChild(row);
                }
                index++;
            }

            // Save selected surahs to local storage
            const selectedSowarsArray = Array.from(selectedSowars);
            localStorage.setItem('selectedSowars', JSON.stringify(selectedSowarsArray));
        }

        function deleteRow(sowar) {
            const row = document.querySelector(`#favoritesTableBody tr[data-sowar="${sowar}"]`);
            if (row) {
                row.remove();
                // Uncheck checkbox associated with removed surah
                const checkbox = document.querySelector(`input[name="sowars"][value="${sowar}"]`);
                if (checkbox) {
                    checkbox.checked = false;
                }
            }
        }

        // Function to load selected surahs from local storage
        function loadFromLocalStorage() {
            const selectedSowars = JSON.parse(localStorage.getItem('selectedSowars'));
            if (selectedSowars) {
                for (const sowar of selectedSowars) {
                    const checkbox = document.querySelector(`input[name="sowars"][value="${sowar}"]`);
                    if (checkbox) {
                        checkbox.checked = true;
                    }
                }
            }
            // Automatically add favorites when page loads
            addToFavorites();
        }

        // Call loadFromLocalStorage function when the page loads
        window.onload = function() {
            loadFromLocalStorage();
        };
    </script>
    </html>
    """ 
    #render favorite page template
    
    return render_template_string(template)

# mawaket route
@mawaket_blueprint.route('/mawaket.html', methods=['GET', 'POST'])
def mawaket():
    #mawaket html code
    template ="""
  <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مواقيت الصلاة</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background: url('static/masjed-img.jpg') no-repeat center center fixed;
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

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            padding: 8px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #3498db;
            color: white;
        }
    </style>
</head>
<body>
<div class="container">
    <h1 class="my-5">مواقيت الصلاة</h1>
    <table>
        <thead>
        <tr>
            <th>الصلاة</th>
            <th>الوقت</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <td>الفجر</td>
            <td>٣:٥٦ صباحا</td>
        </tr>
        <tr>
            <td>الظهر</td>
            <td>١٢:٣٤ مساءً</td>
        </tr>
        <tr>
            <td>العصر</td>
            <td>٤:١٩ مساءً</td>
        </tr>
        <tr>
            <td>المغرب</td>
            <td>٧:٣٦ مساء</td>
        </tr>
        <tr>
            <td>العشاء</td>
            <td>٩:١٣ مساء </td>
        </tr>
        </tbody>
    </table>
</div>
<p style="position:fixed;bottom:0;">&#169; COPYRIGHTS 2024 MM</p>
</body>
</html>

    """
    #render mawaket
    return render_template_string(template)

#define zekr route
@zekr_blueprint.route('/zekr.html', methods=['GET', 'POST'])
def zekr():
    #zekr html code
    template ="""
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>مواقيت الصلاة</title>
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

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        th, td {
            padding: 8px;
            text-align: center;
            border-bottom: 1px solid #ddd;
        }

        th {
            background-color: #3498db;
            color: white;
        }
    </style>
</head>
<body>
<div class="container">
    <h1 class="my-5">افضل الاذكار</h1>
    <p style="display:flex;justify-content:center;align-items:center;">أذكار الصباح:<br>
قراءة آية الكرسي (مرة واحدة).<br>
قراءة سورة الإخلاص والمعوذتين (ثلاث مرات لكل سورة).<br>
“أَصْبَحْنا وَأَصْبَحَ المُلْكُ لله وَالحَمدُ لله، لا إلهَ إلاّ اللهُ وَحدَهُ لا شَريكَ لهُ…” (مرة واحدة).<br>
“اللَّهُمَّ مَا أَصْبَحَ بِي مِنْ نِعْمَةٍ أَوْ بِأَحَدٍ مِنْ خَلْقِكَ، فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ…” (مرة واحدة).<br>
أذكار المساء:<br>
“أَمْسَيْنا وَأَمْسَى المُلْكُ لله وَالحَمدُ لله، لا إلهَ إلاّ اللهُ وَحدَهُ لا شَريكَ لهُ…” (مرة واحدة).<br>
“اللَّهُمَّ أَنْتَ رَبِّي، لا إِلهَ إِلاَّ أَنْتَ، خَلَقْتَني وأَنَا عَبْدُكَ…” (مرة واحدة).<br>
أذكار النوم:<br>
“بِاسْمِكَ اللَّهُمَّ أَمُوتُ وَأَحْيَا” (عند النوم).<br>
“الحَمْدُ للهِ الَّذِي أَحْيَانَا بَعْدَ مَا أَمَاتَنَا وَإِلَيْهِ النُّشُورُ” (عند الاستيقاظ).<br>
أذكار أخرى:<br>
“لا إلهَ إلاّ اللهُ وَحدَهُ لا شَريكَ لهُ، لهُ المُلْكُ ولهُ الحَمْدُ وهُوَ على كلّ شَيءٍ قدير” (مئة مرة في اليوم).<br>
“سُبْحَانَ اللهِ وَبِحَمْدِهِ” (مئة مرة في اليوم).<br>
هذه بعض الأذكار التي يمكن للمسلم قولها يوميًا للحفاظ على ذكر الله والتقرب منه</p>
</div>
<p style="position:fixed;bottom:0;">&#169; COPYRIGHTS 2024 MM</p>
</body>
</html>
    """
    #render zekr template
    return render_template_string(template)

#define aswat route 
@aswat_blueprint.route('/aswat.html', methods=['GET', 'POST'])
def aswat():
    #aswat html code
    template ="""
    <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>سورة البقرة</title>
<style>
    /* Style for the audio player */
    audio {
        width: 100%;
        max-width: 300px;
        margin: 20px auto;
        display: block;
    }
    button {
        display: block;
        margin: 20px auto;
        padding: 10px 20px;
        background-color: #007bff;
        color: #fff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
    body {
            background: url('/static/masjed-img.jpg') no-repeat center center fixed;
            background-size: cover;
            margin: 0;

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
</style>
</head>
<body>

<audio controls id="audioPlayer">
    <source src="/static/002.mp3" type="audio/mpeg">
</audio>

<button onclick="playAudio()">تشغيل</button>
<button onclick="stopAudio()">ايقاف</button>
<button onclick="restartAudio()">اعادة</button>
<script>
    // Function to play the audio
    function playAudio() {
        var audio = document.getElementById("audioPlayer");
        audio.play();
    }
    var audio = document.getElementById("audioPlayer");
    var pausedTime = 0;

    function stopAudio() {
        pausedTime = audio.currentTime;
        audio.pause();
    }

    function restartAudio() {
        audio.currentTime = 0; // Reset audio to the beginning
        audio.play();
    }

</script>

</body>
</html>

    """
    #render aswat template
    return render_template_string(template)

#define masb7a route

@masb7a_blueprint.route('/masb7a.html', methods=['GET', 'POST'])
def masb7a():
    #masb7a html code
    template ="""
    <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>سورة البقرة</title>
<style>  
body {
    background: url('/static/masjed-img.jpg') no-repeat center center fixed;
    background-size: cover;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    height: 100vh; /* Set to 100% of viewport height */
    margin: 0; /* Remove default margin */
}

button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-bottom: 10px; /* Add margin between buttons */
}

button:hover {
    background-color: #0056b3;
}

.counter {
    font-size: 18px;
    margin-bottom: 5px; /* Add margin between counter and button */
}
</style>
</head>
<body>
<h1>المسبحة</h1>

<div>
    <button onclick="incrementCounter('subhanallah')">سبحان الله</button>
    <span id="subhanallahCounter">0</span>
</div>

<div>
    <button onclick="incrementCounter('alhamdulillah')">الحمد لله</button>
    <span id="alhamdulillahCounter">0</span>
</div>

<div>
    <button onclick="incrementCounter('allahuakbar')">الله أكبر</button>
    <span id="allahuakbarCounter">0</span>
</div>

<button onclick="resetCounters()">اعادة ضبط</button>

<script>
    // Function to increment the counter for the specified button
    function incrementCounter(button) {
        var counterElement = document.getElementById(button + 'Counter');
        var currentCount = parseInt(counterElement.innerText);
        counterElement.innerText = currentCount + 1;
    }

    // Function to reset all counters to 0
    function resetCounters() {
        document.getElementById('subhanallahCounter').innerText = '0';
        document.getElementById('alhamdulillahCounter').innerText = '0';
        document.getElementById('allahuakbarCounter').innerText = '0';
    }
</script>
</body>
</html>

    """
    #render masb7a template
    return render_template_string(template)

#register all pages blueprints in order to render
app.register_blueprint(favorites_blueprint)
app.register_blueprint(mawaket_blueprint)
app.register_blueprint(zekr_blueprint)
app.register_blueprint(aswat_blueprint)
app.register_blueprint(masb7a_blueprint)
# run main.py app 
if __name__ == '__main__':
    app.run(debug=True)
