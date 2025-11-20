@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Flask Demo</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #6EE7B7, #3B82F6);
                    margin: 0;
                    padding: 0;
                    color: white;
                }
                .container {
                    max-width: 900px;
                    margin: auto;
                    margin-top: 50px;
                    background: rgba(0, 0, 0, 0.4);
                    padding: 30px;
                    border-radius: 15px;
                    box-shadow: 0 0 20px rgba(255,255,255,0.4);
                }
                h1 {
                    font-size: 42px;
                    margin-bottom: 5px;
                }
                p.subtitle {
                    margin-top: -10px;
                    font-size: 18px;
                }
                .endpoint-card {
                    background: rgba(255,255,255,0.15);
                    padding: 15px;
                    margin: 10px 0;
                    border-radius: 10px;
                    transition: 0.3s;
                }
                .endpoint-card:hover {
                    background: rgba(255,255,255,0.3);
                    transform: scale(1.02);
                }
                a {
                    color: #FFD700;
                    text-decoration: none;
                    font-weight: bold;
                }
                footer {
                    text-align: center;
                    margin-top: 20px;
                    font-size: 14px;
                }
            </style>
        </head>

        <body>
            <div class="container">
                <h1>🚀 DevOps Flask Demo</h1>
                <p class="subtitle">A modern microservice deployed using Jenkins CI/CD pipeline.</p>

                <h2>📌 Available API Endpoints</h2>

                <div class="endpoint-card">
                    <strong>GET</strong> — <a href="/items" target="_blank">/items</a>
                    <p>Fetch all items</p>
                </div>

                <div class="endpoint-card">
                    <strong>GET</strong> — /items/&lt;id&gt;
                    <p>Fetch a specific item</p>
                </div>

                <div class="endpoint-card">
                    <strong>POST</strong> — /items
                    <p>Add a new item (Use Postman)</p>
                </div>

                <div class="endpoint-card">
                    <strong>PUT</strong> — /items/&lt;id&gt;
                    <p>Update an item (Use Postman)</p>
                </div>

                <div class="endpoint-card">
                    <strong>DELETE</strong> — /items/&lt;id&gt;
                    <p>Delete an item</p>
                </div>

                <div class="endpoint-card">
                    <strong>GET</strong> — <a href="/health" target="_blank">/health</a>
                    <p>Health status</p>
                </div>

                <div class="endpoint-card">
                    <strong>GET</strong> — <a href="/version" target="_blank">/version</a>
                    <p>Current application version</p>
                </div>

                <footer>✨ Auto-Deployed using Jenkins | Docker | CI/CD Pipeline</footer>
            </div>
        </body>
    </html>
    """
