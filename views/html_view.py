import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")



def html_response(handler, template_file, headers, rows):
    template_path = os.path.join(TEMPLATES_DIR, template_file)
    with open(template_path, "r") as f:
        template = f.read()

    # Render table rows
    row_html = ""
    for row in rows:
        row_html += "<tr>"
        for cell in row:
            row_html += f"<td>{cell}</td>"
        row_html += f"""
            <td>
                <form method='POST' action='/users/edit' style='display:inline;'>
                    <input type='hidden' name='id' value='{row[0]}'>
                    <input type='submit' value='Edit'>
                </form>
                <form method='POST' action='/users/delete' style='display:inline;' onsubmit="return confirm('Delete this user?');">
                    <input type='hidden' name='id' value='{row[0]}'>
                    <input type='submit' value='Delete'>
                </form>
            </td>
        """
        row_html += "</tr>"

    header_html = "".join([f"<th>{h}</th>" for h in headers]) + "<th>Actions</th>"

    html = template.replace("{{headers}}", header_html).replace("{{rows}}", row_html)

    handler.send_response(200)
    handler.send_header("Content-Type", "text/html")
    handler.end_headers()
    handler.wfile.write(html.encode())