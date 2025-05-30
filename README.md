<h1>🛒 Samsung E-commerce Checkout Automation Guide</h1>
<p>This project automates adding products to the cart on Samsung India using internal API endpoints. Full purchase flow is supported via optional scripts.</p>

<div class="note">
  <strong>⚠️ Note:</strong> This guide is meant for <strong>educational</strong> and <strong>automation demonstration</strong> purposes. Target: <a href="https://www.samsung.com/in" target="_blank">Samsung India</a>
</div>

 <strong>⚠️ Disclaimer:</strong> This script is provided for <strong>educational purposes only</strong>. 
  I am <strong>not responsible</strong> for any misuse, account bans, or damages caused by using this tool. 
  Use at your own risk.

  <div>
    <img src="screenshots/ss (1).jpg" alt="Screenshot 1" style="width:200px; height:150px; object-fit: cover;" />
    <img src="screenshots/ss (2).jpg" alt="Screenshot 2" style="width:200px; height:150px; object-fit: cover;" />
    <img src="screenshots/ss (3).jpg" alt="Screenshot 3" style="width:200px; height:150px; object-fit: cover;" />
    <img src="screenshots/ss (4).jpg" alt="Screenshot 4" style="width:200px; height:150px; object-fit: cover;" />
    <img src="screenshots/ss (5).jpg" alt="Screenshot 5" style="width:200px; height:150px; object-fit: cover;" />
    <img src="screenshots/ss (6).jpg" alt="Screenshot 6" style="width:200px; height:150px; object-fit: cover;" />
  </div>

<h2>📦 <code>add2cart.py</code> — Add Product to Cart</h2>

<h3>✅ Features</h3>
<ul>
  <li>Add product using SKU</li>
  <li>Returns cart summary with pricing</li>
  <li>Prints product and cart details</li>
</ul>

<h3>🧪 Requirements</h3>
<ul>
  <li>Python 3.x</li>
  <li><code>requests</code> library: <code>pip install requests</code></li>
  <li>Session cookies + JWT token</li>
</ul>

<h2>⚙️ How to Use</h2>

<h3>1. Install Dependencies</h3>
<pre><code>pip install requests</code></pre>

<h3>2. Get Headers & Cookies</h3>
<p>Use browser Developer Tools (F12 → Network tab) while logged in to <strong>samsung.com/in</strong>. Capture a request and extract:</p>

<h4>Required Headers:</h4>
<pre><code>x-ecom-jwt: YOUR_JWT_HERE
x-client-request-id: UUIDv4 (generate using uuid module or browser)
x-ecom-app-id: pwa
User-Agent: Your browser's User-Agent string
</code></pre>

<h4>Required Cookies:</h4>
<ul>
  <li><code>deliveryPincode</code></li>
  <li><code>s_ecom_scid</code></li>
  <li><code>ecom_vi2_IND</code></li>
  <li><code>ecom_session_id2_IND</code></li>
  <li><code>jwt_IND</code></li>
</ul>

<div class="warning">
  ⚠️ <strong>Session cookies and JWT expire</strong>. Refresh them as needed.
</div>

<h3>3. Run the Script</h3>
<pre><code>python add2cart.py</code></pre>

<h4>Sample Input:</h4>
<pre><code>Enter the SKU to add to cart: SM-M356BLBB
Enter the Quantity: 1</code></pre>

<h4>Sample Output:</h4>
<pre>
========================================
🛒 PRODUCT ADDED TO CART SUCCESSFULLY
========================================

📱 PRODUCT DETAILS:
• SKU: SM-M356BLBB
• Color: Waterfall Blue
• Storage: 128GB
• Memory: 6GB

💰 CART SUMMARY:
• Cart ID: 0645xxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
• Total: ₹22,418.82
</pre>

<hr>

<h2>🧾 Want Full Automation?</h2>

<p>For complete checkout automation:</p>
<table>
  <thead>
    <tr><th>Script</th><th>Description</th></tr>
  </thead>
  <tbody>
    <tr><td><code>billing-info.py</code></td><td>Sets billing address and GST details</td></tr>
    <tr><td><code>checkout.py</code></td><td>Finalizes and shares payment link</td></tr>
  </tbody>
</table>

<p><strong>Not included for free.</strong> Buy from:</p>
<p>👉 <a href="https://www.buymeacoffee.com/garurprani/e/415688" target="_blank">https://www.buymeacoffee.com/garurprani/e/415688</a></p>

<hr>

<h2>🔐 Authentication Overview</h2>

<p>The script relies on session-based authentication:</p>
<ul>
  <li><strong>Cookies</strong> – active session values</li>
  <li><strong>JWT Token</strong> – passed via <code>x-ecom-jwt</code></li>
  <li><strong>Headers</strong> – User-Agent, Accept, etc.</li>
</ul>

<h3>Header Sample:</h3>
<pre><code>{
  "x-ecom-jwt": "YOUR_TOKEN",
  "x-client-request-id": "UUID",
  "x-ecom-app-id": "pwa",
  "User-Agent": "Mozilla/5.0 ..."
}</code></pre>

<hr>

<h2>🛠️ Troubleshooting</h2>
<table>
  <thead>
    <tr><th>Error</th><th>Cause</th><th>Fix</th></tr>
  </thead>
  <tbody>
    <tr><td>401 Unauthorized</td><td>Expired JWT/cookies</td><td>Get new session headers</td></tr>
    <tr><td>400 Bad Request</td><td>Payload mismatch</td><td>Verify required JSON fields</td></tr>
    <tr><td>Product not serviceable</td><td>Pincode/SKU mismatch</td><td>Try other pincodes or check stock</td></tr>
  </tbody>
</table>

<hr>

<h2>📌 FAQ</h2>

<h4>❓ Can I add multiple products?</h4>
<p>Yes, modify the <code>line_items</code> list with multiple SKUs.</p>

<h4>❓ How to extract session values?</h4>
<ol>
  <li>Login to samsung.com/in</li>
  <li>Open Dev Tools → Network tab</li>
  <li>Perform add-to-cart</li>
  <li>Copy headers + cookies from request</li>
</ol>

<h4>❓ Can I use it for other regions?</h4>
<p>No. It’s tailored for India. You’d need to change domain and payload structure for other countries.</p>

<hr>

<h2>📣 Support / Contact</h2>

<p>📧 DM: <a href="https://www.fiverr.com/garurprani" target="_blank">@garurprani on Fiverr</a></p>
<p>☕ Buy full scripts: <a href="https://www.buymeacoffee.com/garurprani/e/415688" target="_blank">https://www.buymeacoffee.com/garurprani/e/415688</a></p>

</body>
</html>
