import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
#from cv_thread import CvThread

app = Flask(__name__)
app.static_folder = 'static'


@app.route('/')
def hello():
    return ("hello")


@app.route('/method')
def method():
    return render_template('/index.html')


@app.route('/result')
def result():
    search_result = []
    for filename in os.listdir('static/result'):
        search_result.append('static/result/'+filename)
    source = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>MY WEBSITE</title>
    <link href="static/styles.css" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" />
    <!-- include libraries(jQuery, bootstrap) -->
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css" rel="stylesheet" />
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

    <!-- include summernote css/js -->
    <link href="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.css" rel="stylesheet" />
    <script src="https://cdn.jsdelivr.net/npm/summernote@0.8.18/dist/summernote.min.js"></script>

    </head>

    <body>
    <header>
        <div id="title">MY WEBSITE</div>
    </header>

    <div id="container">
        <div id="content">
        <div id="result">
            <div class="result-title">
            <!-- 제목 -->
            <div id="result-title-text">RESULTS</div>
            </div>
            <div style="
                width: 100%;
                height: 600px;
                background-color: blue;
                display: flex;
                ">
            <div style="
                    position: relative;
                    width: 10%;
                    height: 100%;
                    background-color: #fafafa;
                ">
                <!-- 화살표 -->
                <div style="
                    position: absolute;
                    width: 100%;
                    height: 100px;
                    top: 0;
                    bottom: 0;
                    margin: auto 0;
                    ">
                <div class="arrow-container">
                    <a href="https://sports.news.naver.com/index.nhn" style="color: black">
                    <i class="fa-solid fa-circle-arrow-up"></i>
                    </a>
                </div>
                <br />
                <div class="arrow-container">
                    <a href="https://sports.news.naver.com/wfootball/index" style="color: black">
                    <i class="fa-solid fa-circle-arrow-down"></i>
                    </a>
                </div>
                </div>
            </div>
            <div style="width: 60%; height: 100%; background-color: #d8d8d8; overflow: hidden;">
                <!-- 사진 -->
                <img src="{}" alt="No Results" style="width: 100%;">
            </div>
            <div style="
                    width: 30%;
                    height: 100%;
                    background-color: #848484;
                    position: relative;
                ">
                <!-- 설명 -->
                <div style="
                    position: absolute;
                    top: 0;
                    bottom: 0;
                    left: 0;
                    right: 0;
                    width: 100%;
                    height: 128px;
                    margin: auto;
                    ">
                <ul style="
                        list-style-type: none;
                        font-size: 1.2em;
                        padding-left: 10px;
                    ">
                    <li>Name : Vans - 어센틱 레드</li>
                    <br />
                    <li>Price : 69,000Won</li>
                    <br />
                    <li>Size : 250 - 310</li>
                </ul>
                </div>
            </div>
            </div>
            <div class="result-title">
            <!-- 구매처 -->
            <div style="
                    background-color: #a4a4a4;
                    height: 100%;
                    position: relative;
                ">
                <div id="buy-place">구매처 :</div>
            </div>
            </div>
        </div>
        <form id="search" action="/upload" method="POST" enctype="multipart/form-data">
            <input type="submit" id="search-text" value="searching" />
            <div style="
                width: 100%;
                height: 400px;
                border: 1px solid gray;
                margin-top: 30px;
                ">
            <!-- <div id="summernote" style="width: 100%; height: 100%"></div> -->
            <input type="file" name="file">
            </div>
            <div style="width: 100%; height: 100px; margin-top: 30px; padding: 10px">
            태그
            </div>
        </form>
        </div>
    </div>

    <footer>
        <div id="copyright">Copyright &copy; 정명훈 2022</div>
    </footer>
    </body>

    </html>
    """.format(search_result[0])
    return source


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        filepath = 'static/uploaded_imgs'
        file.save(os.path.join(filepath, filename))
        return method()


if __name__ == '__main__':
    #cv = CvThread()
    # cv.start()
    app.run(port=5000, debug=True)
