from flask import Flask, render_template, request, redirect, url_for, Response
import yt_dlp

app = Flask(__name__)

# Dummy code
CORRECT_CODE = "123456"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/verify", methods=["POST"])
def verify():
    code = request.form.get("code")
    if code == CORRECT_CODE:
        return redirect(url_for("video"))
    return render_template("index.html", error="Invalid code. Please try again.")


@app.route("/video")
def video():
    return render_template("video.html")


@app.route("/stream")
def stream():
    youtube_url = "https://www.youtube.com/watch?v=tLn0bq2mbVU"

    def get_video_stream():
        ydl_opts = {
            "format": "best",  
            "noplaylist": True,
            "quiet": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            video_url = info.get("url")
            if not video_url:
                raise ValueError("Could not extract video URL.")
            return video_url

    try:
        video_stream_url = get_video_stream()
        return redirect(video_stream_url)  
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
