import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")


def render_template(template_name, headers, rows):
    path = os.path.join(TEMPLATES_DIR, template_name)
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    header_html = "".join([f"<th>{h}</th>" for h in headers])

    row_html = ""
    for row in rows:
        row_html += "<tr>" + "".join([f"<td>{col}</td>" for col in row]) + "</tr>"

    html = html.replace("{{headers}}", header_html)
    html = html.replace("{{rows}}", row_html)

    return html


def html_response(handler, template_name, headers, rows):
    handler.send_response(200)
    handler.send_header("Content-type", "text/html")
    handler.end_headers()

    html = render_template(template_name, headers, rows)
    handler.wfile.write(html.encode())