<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    
</head>
<body>

<h1>Spam Filter </h1>

<h2>Overview</h2>
<p>This Spam Filter Project is a sophisticated implementation of a Naive Bayes classifier designed to differentiate between spam and non-spam (ham) emails. The goal is showcase practical applications of probability theory and natural language processing (NLP) techniques built in Python.</p>

<p>At its core, the project utilizes a probabilistic model to analyze the contents of an email and predict its classification based on the frequency of specific words. It employs the following key components:</p>

<ul>
    <li><strong>Email Tokenization:</strong> This step involves processing the raw text of an email to extract meaningful tokens (words or other significant text elements). The <code>load_tokens</code> function reads an email file and breaks down its content into a list of tokens, which are then used to compute the probabilities of being spam or ham.</li>
    <li><strong>Log Probability Calculation:</strong> The <code>log_probs</code> function calculates the logarithmic probabilities of tokens appearing in spam and ham emails, incorporating smoothing to handle zero-frequency issues. This probabilistic approach helps in dealing with the vast diversity of language used in emails.</li>
    <li><strong>Classification:</strong> The <code>SpamFilter</code> class integrates these components, using the computed log probabilities to classify new emails. It evaluates whether an email is more likely to be spam or ham based on the cumulative probabilities of its tokens.</li>
    <li><strong>Indicative Tokens Identification:</strong> Additionally, the SpamFilter provides functionality to identify the most indicative tokens of spam or ham, helping in understanding the characteristics of emails that most influence the classification decision.</li>
</ul>

<p>This project exemplifies the application of machine learning principles in building a simple yet effective spam detection system, offering a hands-on experience in developing, training, and testing a machine learning model with real-world data.</p>

<h2>Setup</h2>
<p>No external dependencies are required to run this project, as it uses Python's standard library. Ensure Python 3 is installed on your system.</p>

<h2>Running the Spam Filter</h2>
<p>To run the spam filter:</p>
<ol>
    <li>Ensure your dataset is structured with separate directories for spam and ham emails.</li>
    <li>Initialize the SpamFilter with paths to your spam and ham datasets and a smoothing parameter.</li>
    <li>Use the <code>is_spam</code> method to classify new emails.</li>
</ol>

<h2>Testing</h2>
<p>Tests are located in the <code>tests</code> directory. To run them, execute the following command in the terminal:</p>
<pre><code>python -m unittest discover tests</code></pre>


</body>
</html>
