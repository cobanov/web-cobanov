from flask import Flask, render_template, abort
import os

app = Flask(__name__)


def get_blog_posts():
    blog_dir = os.path.join(app.root_path, "templates", "blog_posts")
    blog_files = [f for f in os.listdir(blog_dir) if f.endswith(".html")]

    # Mapping filenames to titles
    blog_posts = {
        "generative_art": "Generative Art: A Gentle Introduction",
        "bitter_sweet": "Bitter Sweet",
		"piracy": "piracy",
    }

    blog_posts = {
        key: blog_posts[key] for key in blog_posts if f"{key}.html" in blog_files
    }

    return blog_posts


def get_helper_posts():
    helpers_dir = os.path.join(app.root_path, "templates", "helpers")
    helpers_files = [f for f in os.listdir(helpers_dir) if f.endswith(".html")]

    # Mapping filenames to titles
    helpers_posts = {
        "new_ubuntu": "New Ubuntu Installation",
        "one_liners": "One Liners",
    }

    helpers_posts = {
        key: helpers_posts[key]
        for key in helpers_posts
        if f"{key}.html" in helpers_files
    }

    return helpers_posts


@app.route("/")
def home():
    blog_posts = get_blog_posts()
    return render_template("index.html", posts=blog_posts)


# @app.route("/about")
# def about():
#     return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


# @app.route("/contact")
# def contact():
#     return render_template("contact.html")


@app.route("/blog")
def blog():
    blog_posts = get_blog_posts()
    return render_template("blog.html", posts=blog_posts)


@app.route("/helpers")
def helpers():
    helpers_posts = get_helper_posts()
    return render_template("helpers.html", posts=helpers_posts)


@app.route("/blog/<post_name>")
def blog_post(post_name):
    blog_posts = get_blog_posts()
    if post_name in blog_posts:
        return render_template(
            f"blog_posts/{post_name}.html", title=blog_posts[post_name]
        )
    else:
        abort(404)


@app.route("/helpers/<post_name>")
def helper_post_post(post_name):
    all_posts = get_helper_posts()
    if post_name in all_posts:
        return render_template(f"helpers/{post_name}.html", title=all_posts[post_name])
    else:
        abort(404)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
