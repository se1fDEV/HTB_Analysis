<h1>HTB_Analysis</h1>

<p>HTB_Analysis is a Python script designed for testing and  LDAP injections and similar vulnerabilities through fuzzing LDAP with a specified wordlist or charset.</p>
<p>This one will also help to automate and facilitate the walkthrough of "Analysis" machine<p>

<h2>Getting Started</h2>

<p>These instructions will guide you on how to set up and run HTB_Analysis on your local machine for development and testing purposes.</p>

<h3>Prerequisites</h3>

<ul>
    <li>Ensure you have the following installed before proceeding:</li>
    <ul>
        <li>Python 3</li>
        <li>pip (Python package manager)</li>
        <li>Ability to modify your system's <code>/etc/hosts</code> file (for host resolution)</li>
    </ul>
</ul>

<h3>Installation</h3>

<ol>
    <li><strong>Clone the Repository</strong></li>
    <p>Clone this repository to your local machine:</p>
    <pre><code>git clone https://github.com/se1fDEV/HTB_Analysis.git</code></pre>
    <li><strong>Install Required Python Libraries</strong></li>
    <p>Change to the cloned directory and install necessary Python libraries:</p>
    <pre><code>cd HTB_Analysis
pip install -r requirements.txt</code></pre>
    <li><strong>Configure Hosts File</strong></li>
    <p>Modify your <code>/etc/hosts</code> file to include the IP address of the target machine. This is required for domain resolution for <code>internal.analysis.htb</code>. Add the following line:</p>
    <pre><code>10.129.10.10    analysis.htb internal.analysis.htb</code></pre>
    <p>Note: Editing <code>/etc/hosts</code> typically requires administrator privileges.</p>
</ol>

<h3>Running the Script</h3>

<p>Execute the script with the following command:</p>
<pre><code>python HTB_ldap_fuzzer.py</code></pre>

<p>Upon prompt, enter the path to your wordlist or charset. Press Enter to use the default wordlist provided.</p>
![HTB_Analysis_code](https://github.com/se1fDEV/HTB_Analysis/assets/154564062/a68b7d46-d92b-4166-ac64-e6448a2cd043)

<h2>License</h2>

<p>This project is licensed under the MIT License.</p>

![HTB_Analysis_img](https://github.com/se1fDEV/HTB_Analysis/assets/154564062/774a1fd6-0fcb-4c4f-8c1d-6f61b6796654)


