---
layout: page
<!--title: Software Technology-->
<!--permalink: /index/-->
---

<center>
<img src="./assets/images/flowchart.png" alt="drawing" width="400"/>
</center>

&nbsp;<p>

# Search the site
<form action="{{ page.url | relative_url }}">
  <div class="tipue_search_left"><img src="{{ "/assets/tipuesearch/search.png" | relative_url }}" class="tipue_search_icon"></div>
  <div class="tipue_search_right"><input type="text" name="q" id="tipue_search_input" pattern=".{3,}" title="At least 3 characters" required></div>
  <div style="clear: both;"></div>
</form>

<div id="tipue_search_content"></div>

<script>
$(document).ready(function() {
  $('#tipue_search_input').tipuesearch();
});
</script>


Welcome to the one-stop lecture notes for Software Technology stream, School of Computing, Macquarie University.

If you identify a typo, click on "Edit (README for details)" and hop to the bottom of the Github page for explanation on how to fork, edit, commit and open a pull request.

If you have any suggestions, please email me at [gaurav.gupta@mq.edu.au](mailto:gaurav.gupta@mq.edu.au).