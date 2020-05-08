<div style="display: none">If you are seeing this from Github, there is a user-friendly version of this page with an embeded searchbar at: http://joyce-chen.github.io/persona5-negotiation/<br><br>
</div>

<div style="display: flex; flex-wrap: wrap;">
	<div style="flex: 3" class="input-group">
		<input class="form-control py-2 border-right-0 border" type="text" id="searchBar" onkeyup="filterQuestions()" placeholder="Search for questions or responses.." title="Type in a question or response">
		<span class="input-group-append">
			<div class="input-group-text bg-transparent"><i class="fa fa-search"></i></div>
		</span>
	</div>

	<div style="flex: 1; text-align: center;">
		<label class="switch">
			<input type="checkbox" onClick="toggleCompact()">
			<span class="slider round"></span>
		</label>
	</div>
</div>

<script>
function filterQuestions() {
    var input, filter, div, table, tr;
    input = document.getElementById("searchBar");
    filter = input.value.toUpperCase();
    div = document.getElementById("questions");
	table = div.getElementsByTagName("table");
    for (i = 0; i < table.length; i++) {
		var question = table[i].getElementsByTagName("th")[0].textContent.toUpperCase();
		var answerOne = table[i].getElementsByTagName("td")[5].textContent.toUpperCase();
		var answerTwo = table[i].getElementsByTagName("td")[10].textContent.toUpperCase();
		var answerThree = table[i].getElementsByTagName("td")[15].textContent.toUpperCase();
		
		if (question.indexOf(filter) > -1 || answerOne.indexOf(filter) > -1 || answerTwo.indexOf(filter) > -1 || answerThree.indexOf(filter) > -1) {
			table[i].style.display = "";
		} else {
			table[i].style.display = "none";
		}
    }
}

function toggleCompact() {
	var text = document.getElementsByClassName("text");
	var symbol = document.getElementsByClassName("symbol");
	for (var i = 0; i < text.length; i++) {
		if (text[i].style.display === "none") {
			symbol[i].style.display = "none";
			text[i].style.display = "block";
		} else {
			symbol[i].style.display = "block";
			text[i].style.display = "none";
		}
	}

	var extra = document.getElementsByClassName("extra");
	for (var i = 0; i < extra.length; i++) {
		if (extra[i].style.display === "none") {
			extra[i].style.display = "inline";
		} else {
			extra[i].style.display = "none";
		}
	}
}
</script>

<div id="questions">
<table class="X">
	<tr>
		<th colspan="5">A bad rep spreads like wildfire. If I were you, I'd quit all this nonsense. What's the point?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't know any other way.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">After confronting me like this... Are you that kind of human too?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's not my style.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You've got a point.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You've grown old.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Ah, it's a shame. If I'd taken this seriously from the start, I wouldn't be in this sorry state.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Making excuses?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Then get serious now.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I wasn't trying either.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Ah, so I suppose you commit such extreme acts because you know you won't be punished harshly...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm sorry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Age doesn't matter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This isn't extreme.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Ain't people your age suppose'ta be out on dates and stuff instead?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Right after this, kid.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Such a rude little boy...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Dating's not important.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">And if that's the case, why don't you just stop this futile endeavor? It's meaningless...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You have a point there...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't stop.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll find meaning in it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Are all the kids these days doin' stuff like this?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Yeah, we sure are.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I thought this up myself.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Want to join in?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Are there only men's versions? Where did you get it?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Do you want it?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Internet shopping.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's not available for sale.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Are you bored?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Yes, I'm bored.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm actually pretty busy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I never thought about it.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Are you fighting to help or protect the world or something?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That?s right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I won't tell you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It pays the bills.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">As far as you're concerned, what kind of person was I to you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>My rival.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nobody, really.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It doesn't matter.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...But be-hee-fore all that, let's enjoy a little chat, ho!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>All right, I suppose.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There's no need for that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>[...]</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">But before you do, do something funny. What can you do?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Impressions</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Making funny faces</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">But is it fair to the others if I find this happiness, leaving them all in the dust?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I think it's fine.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What's wrong with that?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're too self-conscious.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">But I've been around the block, so I know--there's something else you want from me, isn't there?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm acting on a whim.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I love the elderly.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I just want you to die happy.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">But I've got a catch phrase that I'm famous for.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Hee-ho!</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Hee-haw!</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Personaaa!</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">But what if I ripped your body apart? ...What color blood would come pouring out?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Red.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Green.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I never bleed or cry.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Can you sacrifice yourself in order to demonstrate your adoration of our Father?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I can.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't adore him.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Care to explain yourself? I certainly hope you have a good reason for this boorish treatment.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It'd take a while to explain.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>There's no need to explain.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just shut up...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">C'mon, what's with the mask? Kinda cringy, don'tcha think?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Sure is.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Shut up...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm secretly a kid.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Confess your sins.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I apologize.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I think... I was wrong.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No chance.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Could this be what humans call a proposal...?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm surprised you know.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, it's not.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's a myth.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Couldn't ya at least make me a cup of tea or somethin'? Hell, that'd be real polite.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>So sorry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Brew your own.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm not known for being polite.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Did I just see your hand shaking? Are you OK?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm a bit chilly, but...</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm a little scared...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Shut up!</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Did I... lose?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Yup.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Not sure yet.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nah, you totally won.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Didn't you feel like that when you were a kid, too?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's not so bad-olescent.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Being a kid is tough.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't remember.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Do you have a dish you're good at?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Fried rice.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Mystery meat.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What are you saying?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Do you have a lot of friends? Ever feel like the things they do are annoying?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Sometimes.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I have no friends.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Do you know what I speak of?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Sin...?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Please tell me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I've done nothing wrong.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Do you seek friendly competition with a beloved neighbor? Or have you come to destroy a hated foe?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're a beloved neighbor.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're a loathsome foe.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You sound preachy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Do you think they really mean it all the time?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>YES</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, but they say it anyway.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm cuter than most kids.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Doesn't what you're doing bother your conscience?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Now that you mention it...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>...Nope</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm past such things.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Don't take this the wrong way, but man... Bein' a carefree kid sure must be nice.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I want to be a kid forever.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I prefer being an adult.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I wish I was still a baby.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Don't you think expecting your would-be victim to be receptive to your words is unreasonable?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I do.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't think its unfair.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't fret about it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Don't you think it's sad that slang and sayings can grow old and get outdated?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That is sad.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't think so.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That just proves you're old.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">For you to force me to prostrate myself, as one who only seeks your well-being... Is there anything more irrational?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>My apologies.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't want salvation.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Guess what I want you to read to me before you tuck me into bed!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A story about Yakuza.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>[...]</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I have no idea.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Had I known things would turn like this, I'd wish I had found the courage to ask that girl out...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's not too late.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You never had a chance.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll make sure she's happy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Have you made an appointment, ho?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I have.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's not it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just tell me what you know.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...Heed my words. I am not the one you should detest.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's absurd.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll be the judge of that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hell, I got all sortsa girls lined up if you're into that.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Really?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're trying way too hard.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm not interested.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey. Aren't you hungry? Can we take a break and go eat somewhere?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>What do you want to eat?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>If we split the cost.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm on a diet.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey, how about this? If you don't shoot me, then I'll kiss you. Not a bad deal, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Not a bad idea.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't want a kiss.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Have some self-respect.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey, if ya got any medicine, lend me some. One of them painkillers...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Are you OK?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I have some antacids.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That won't change anything?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey, if you got any medicine, lend me some. They're supposed ta work miracles, right...?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Are you OK?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What kind of medicine?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That won't change anything?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey, is my hair flat? Does it look weird?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It looks cute.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's weird looking.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Who cares?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey, let's play a game! Guess what I wanna eat!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Hamburgers.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Humans.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey mister, if I grew up, what do you think the future me would've been like?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A fashionable older woman.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>A weathly housewife.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Living in the darkness.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey, mister, will you give me a yummy snack to eat?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Later.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No way.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What would you like?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey. So whaddya think when you think about the future?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>An average level of happiness.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Live fast, die young.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Nothing.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey, sonny if somethin's been botherin' you. I'm willin' ta give you a listen.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>My relationships...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I smell sweaty.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I have no worries.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...Hey, there's no need for all this, right? Let's drop the drama and just go get something to eat. The thought has crossed your mind, hasn't it? Come on, where would you take me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>An expensive French restaurant.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A busy ramen joint.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A famous pancake place.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Hey. Why aren't you at school?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's a school holiday.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't feel like going.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I actually finished school.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Honestly, aren't I, like, a (?) better girl than those idols?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're more unique.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Idols are the best!</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Who cares about idols?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">How 'bout we have an interview? You're the winner, after all. I'll listen to whatever you gotta say.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I feel great.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I want to aim higher.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Fighting is pointless.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...How 'bout you, sonny? What kinda trip do you wanna take?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A luxury cruise.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't go anywhere.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>A trip to hell.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">How 'bout you? You wanna get married someday?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I do.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>That's impossible.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">How can you do such terrible things to a cute hee-ho like me!?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm sorry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Now that you mention it...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>...Cute?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">How did you find out about me, ho?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Some flyers.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A speciatly site.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Word of mouth.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Humans always want either an autograph or a self-hee, ho. Which is it, ho?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I want an autograph.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want a photo.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Give me your credit card.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Humans talk over drinks, right? How 'bout it? Hell, let me buy you a round, sonny.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Quit messing with me.</td>
		<td class='result'><div class='text'></div><div class='symbol'></div></td>
		<td class='result'><div class='text'></div><div class='symbol'></div></td>
		<td class='result'><div class='text'></div><div class='symbol'></div></td>
		<td class='result'><div class='text'></div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're paying?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm a minor.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I also have loved ones who would miss me. You do catch my meaning, yes?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I just realized that.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I do now.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That doesn't matter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="5">I can't sadden my fans, ho. ...You catch my drift, don't you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm rooting for you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Tell me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You have no fans.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I coulda been a star...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A star?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That's never happening.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Are you giving up?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I don't hate you, No, I don't feel that way at all...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Is that so?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Too late.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Well, I hate you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I fear neither death, nor you.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>In your situation?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're tough.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't push yourself.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...I gotta ask. How do you work out?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I don't really train.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I just have a knack for it.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>At a gym from hell.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I insist you surrender yourself to the authorities.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>This is a misunderstanding.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I apologize.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You've got the wrong idea.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I know when I'm gettin' all sweaty. I'm glistenin', ain't I?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Like a disco ball.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Not at all.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Why does that matter?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I lost. Here I lay, at your feet, at your mercy. Just what do you want from me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Give me something.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Grovel before me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I don't know.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I mean, how does it feel to wave your gun at an enemy who's completely lost the will to fight?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's not bad.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>...I could get used to it.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It pains my heart...</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I need to recover, ho. Don't you feel that way too?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Yeah, sometimes.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Battle is what soothes me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Quit whining.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I occasionally wish to pamper myself as a reward for working hard. How would you do that?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Relax at home.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Go impulse shopping.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Don't be so selfish.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I suppose that's why I feel so confused, child. After all, why am I being treated like this?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Because you resisted.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It can't be helped.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Holidays don't matter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I suppose this "real world" where you come from must be fairly boring.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's really boring.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm always so busy there.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's better than here.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I think dying alone isn't so bad dearie, but isn't living alone in the first place the real tragedy?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I don't think so.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Maybe you're right.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Being alone is a luxury.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I think the way you're treating me is "overfamiliar." I think...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>We are friends.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What's wrong with that?</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's because you're cute.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I wanted to go on vacation, too, before all this happened...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's too bad.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What are you getting at?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You have a boyfriend?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I wish I could see what kind of parents raised you to run loose and wreak havoc like this.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I can't show you now.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I won't show you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Leave my parents out of this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I wish they would leave us old people alone. After all, it's not like we have much time left.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I agree.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Speak for yourself.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There's an aging boom...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I wonder how things might have been between us if cicumstances were different somehow.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>We wouldn't have been enemies.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>We'd have gotten married.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing would've changed.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I wonder how things might have been between us if circumstances had been different somehow?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>We would have dated.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>We'd have gotten married.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing would've changed.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I wonder if us speaking together like this now means that we are somehow connected...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Eh, could be.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I don't think so.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's what we call destiny.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I would never have accepted this task if I knew it would involve this sort of suffering.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's a pity...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Uninformed choices are bad.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Complaining won't help.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If I were to die here, my existence up to this point would be rendered meaningless. But this way of life in this world is all I've ever known.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's not meaningless.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>There are other ways to live.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You had a good run...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If so, then won't you overlook this? Let's make a deal...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>All right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>A deal with the enemy?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't trust you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If that's the plan, well, you better make sure I'm satisfied.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Don't toy with me.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're not making sense.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What would you like?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If that's true, then I don't think there's any real point in killing me...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Of course, there's a point.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're right</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Then who's the real enemy?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If yer gonna kill me, do me a solid and make it quick.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Aren't you scared?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll have some fun first.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I won't make you suffer.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If you ask me, it's a lot more fun ta go chasin' after younger ladies, but...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>This is true.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's not very fun.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You dirty old man.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If you capture me, what you going to do to me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Take pride in capturing you</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Use you to decorate the hall</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Nothing.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If your girlfriend asked if you were free to have dinner with her "friends", what would you say?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Sure.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm busy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">If your parents could see you now, I'm sure it would break their hearts...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You might be right...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This doesn't involve them.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Actually, they'd rejoice.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'll go out with you just for today if there are no strings attached.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>If it pleases you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No strings attached?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I've got enough on my plate...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm a man with a complicated background. The people I know, well...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I want to meet them.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Complicated...?</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Liar.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm a super popular Shadow, you know. My fans won't just sit around and take this, ho.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Please forgive me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Fans?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>So what?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm busy, ho. It's tough being so popular.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You do sound busy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Your popularity won't last.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Who cares?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm inclined to turn you down, but if you still wish to speak, I will perhaps consider it.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You have nothing I want.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Do you have time?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Don't turn me down.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm just putting this out there, but you wouldn't treat me this way if I were younger, right? ...It's true, isn't it?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's not true.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Maybe.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Cougars are all the rage now.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...I'm not going to go easy on you for doing something like this, you know...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm sorry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Prepare for the worst.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>How much do you want?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm not the one you should want to shoot...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You've got a point there...</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's absurd.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Anyone will do.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm sure a miracle's gonna happen to me, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Miracles don't exist.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'd be jealous if it did.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm waiting.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm sure there're other people in the world who'd irritate you more. You know, like-</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Older people trying to look young.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No one bothers me.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I hate everyone.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm thinking that maybe I can be more grandmotherly. How can I go ahead and do that for you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Make me a homemade meal.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Scold me every so often.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You don't have to do anything.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I'm tired of being a kid. Didn't you feel that way when you were little, too?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Sure did.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Not really.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want to be a kid forever.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">In the end, killin' me's just a waste of yer time and energy. You get what I'm sayin', right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>When you put it that way...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's not a waste.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Enemies must be eliminated.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Is it because I'm not acting mature enough? Like, what the heck makes someone mature, anyway?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Being old enough to drink.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Paying your own rent.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Questioning maturity.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Is it 'cause I wasn't a "good boy"?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Yes.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's not why.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Is it not possible for this series of events involving you and me to be attributed to that?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Fair enough.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That is incorrect.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Is it scary to get a shot? Does it make you cry, mister?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I cry like a baby.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I endure it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I like shots.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Is there a reason why I just can't beat you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm younger, that's all.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I've totally got girl power.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Figure it out yourself.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Is there really any benefit for me if I joined with you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I think there is.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I can't promise that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's a matter of feeling.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Isn't that just like when a human woman gets married and moves in with her husband?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I love someone else.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="5">Isn't that kinda... outdated thinking? </th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Sorry. </td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's for your own good. </td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's timeless. </td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">It is to become aware of the gaze of our Father who watches over you with loving grace.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I feel his gaze.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't think so.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">It look like you corner me... But how me know this not trick? How me know you really winning?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Because it's the truth.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's a lie.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't know.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">It'd prolly be a big downer if the birthday boy didn't show to his party, sooo...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Happy birthday.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I had no idea.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This'll be your deathday too.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">It's cliched, but we could talk about life... Ask each other things like what kind of girls we're into...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I like older women.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No preference.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I like men.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...It's fine. Do as you please</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I need your help.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Lick my shoes.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Are you sure it's fine?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">It's hard to tell under the mask, but... you're actually handsome, aren't you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>How did you know?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, not all.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I look ok, I guess.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">It's no fun going home when only my annoying mom and dad are there.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Parents are annoying.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You should love your parents.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Why not come to my place?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">It's pretty rude, man.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>No it isn't.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's part of my face.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>My apologies.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I've been projecting a "don't speak to me" aura towards you.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I noticed.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I didn't feel an "aura".</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>But we may never meet again.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">I've heard that love can bloom anywhere, even on a battlefield. Don't you think that's possible?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Can it?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Definitely not.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What are you saying?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Just thinkin' about hierarchy, you should be showin' me a little more respect, shouldn't you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're right, Senpai.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I never thought about it.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I prefer mutual respect.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Know how they say, "Be kind ta yer elders"? Has no one ever taught you that?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Someone did once.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't want to grow old.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Life's nothing but pain anyways. Just do whatever you want.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You should have stayed home.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You won't die easily.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't get desperate.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Man, I'm about ta be a victim of that too. Hell, does this country even have a future?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It does.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Don't expect it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>The elderly have bad manners.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Maybe I should try something new! I don't want to fall into mediocrity, ho...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're fine as is.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Your act is a bit stale...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Time for a makeover.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...Maybe I'll call the police. Maybe I'll tell 'em that you were worse than you actually were!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Call them. I dare you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Please don't.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It was self-defense.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Maybe kids got spanked a long time ago, but people don't do that anymore, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I didn't know that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You need a good spanking.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Some things are timeless.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Me am really in soup, now. Do what you want. Me am ready if you want grill me, so...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'll make you into soup.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't want to eat you.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll mince you.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Me guessing you have power that me not have. But what is it...?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's my intelligence.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's money.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Girl power.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Me no curse you, but me curse your commander! Me curse the one who order you...!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>This was my choice.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Fighting me is bad luck.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just try to escape.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Me not curse you, but me curse your commander! Me curse the one who order you...!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>This was my choice.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Fighting me is bad luck.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just try to escape.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Me not understand in what way you superior to me...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Youthfulness</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Cuteness</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Luckiness</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Me really want to eat something.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Do not mock me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Same goes for me</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Want to order something?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Me want to ask some recommendations, so me can at least imagine.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Bread soaked in coffee.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't have any.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Hunger is the best spice.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Me want you to give me some nice "words of compassion"-as my rival- as me pass away...!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Die in peace.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Why show mercy to my enemy?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>... I got nothing.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">My chest is beating so fast. What is this feeling?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Are you alright?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're making it up.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's love.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">My horoscope said I was going to have "relationship difficulties" today.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Looks like it came true.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's just a horoscope.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>How is your luck in romance?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">My only choice now... is to retire, ho.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's too far.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>What are your plans?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You had a good run...</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">No matter the crime, humans treat it more lightly if the perpetrator is a minor, do they not?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's not true.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Age doesn't matter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This isn't extreme.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Oh, they're so self-assured that they'll be so successful in the future. Are you like that, child?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's not true.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What's wrong with that?</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Ooh, what if this leaves a scar and it's permanent?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Sorry...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just get plastic surgery.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll take responsibility.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Out of respect for our Father, let us take a moment's respite...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>If you want to.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What do you want to say?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm a minor.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Seriously, cosplaying in a place like this? Are you just really freakin' bored?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I am.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I'm actually very busy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">She said, "I'll buy it for you on the way home," but she didn't but it for me! Isn't that not fair?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's unfair.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Your fault for being tricked.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Be more persistent.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...So, I'm sorry, but can I go and fix my bangs first?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Quit joking around.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're fine as you are.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's pointless.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">So... I'm sorry, but can I go and fix my bangs first? </th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Quit joking around.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're fine as you are.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's pointless.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">So me am going to haunt you for the rest of your life. Me always right behind you...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That would be troublesome.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I could carry that weight.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I wouldn't like that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...So uh, instead of killin' me, you started chattin' with me... You tryin' to get somethin' from me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Yup.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No... Nothing at all...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Dance for me!</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...So? What's going to happen to me now?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You'll be killed.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What do you want to happen?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's a secret.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">So who're you tryin' to impress with that mask?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Nobody.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Shuddup...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm actually still young...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">So why me in this situation right now? Why me at your mercy?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Times have changed.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Humans are powerful.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This is a difficult topic...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">So... You enjoy teasing older women like this?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I had no intention. </td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It is fun, actually.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm serious.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Somethin' bad happen in yer life or somethin', sonny?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's not like that.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I got bad luck.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Something about people putting honey on cucumbers to feel like they're eating fancy cantaloupe?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I follow those tips.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's depressing.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Never heard of that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Sorry, but I want you to go hee-home now. I'm already feeling so tired and weary, ho...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Fine.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You go home.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Taking that into consideration, do you still want me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I didn't think that far.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>The feelings will come.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Tell me, what does "equal footing" mean to you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Not talking down to people.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Sharing household chores.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Splitting all the costs.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">That power, it originates from our Father. Thus, is it not reasonable to repay him for the favor?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I didn't know...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This is my power.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There is no "Father".</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">That's how I feel. And is it not pitiable when one denies one's feelings to oneself?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It is a difficult topic.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>But the outcome is clear.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's mature to admit defeat.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">That's whack, man. Maybe you should get your head checked out.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I probably should.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm fine as is.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're a sore loser.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">The truth is... You're a good person, aren't you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I get that a lot.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Actually... I'm bad.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Are you mocking me?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">The way you treat me, though, is giving me mixed messages. How to you really feel about me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're beautiful.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're scary.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing in particular.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">There something you want say to me, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I want you.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Not really.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Let me touch your paws.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Therefore, I cannot be destroyed. Desist form this pointlessness.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's absurd.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're lying.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">They always give the guy a katsudon! You got anything like that for me!?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Katsudon, coming right up.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm the interrogator here.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I have nothing for you.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">They wear sleeveless shirts in the winter, right? What do you think about that, dearie?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I like it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>They miss seasonal changes.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">This is all some kind of thing for the TV, ho! Where's the camera?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Wow, you got me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>What's all this now?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>This is real.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">This is that "domestic violins" thing, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's "domestic violence."</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What? No, you're wrong...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Um, are things ok at home?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Today I have what you humans call a girl's night out.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Quit messing with me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Should I go instead?</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Girls...?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...Um, this has been buggin' me for a while, but... Is it me, or does something stink?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's just you.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's coming from you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I smell a lie.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...Um, why're you going' for me? Ain't there worse people out there? What kind of guys piss you off?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Slow walkers.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Loud talkers...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Nobody.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...Very well. In the place of our Father, I shall listen to your complaints.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Why can't we end war?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No complaints here.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't get a girlfriend.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Vow that you will use that power in the name of our Father.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'll think about it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No need to be so dramatic.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I decline.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Well, I need to see myself home soon... </th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Just go home.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What do you mean?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't lie to me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Well, I'm still here... That guy is really keeping me waiting.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Life isn't like fairy tales.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just wait a little longer.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You'll never meet him.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">We'll just say you win. So can we stop this?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I feel bad.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't agree with this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Everyone wins.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What are we gonna do, huh?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Tag.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Let's play a video game.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Cruise for chicks.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What are you thinking now?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>How to negotiate..</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>How can I get popular?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What did I do to deserve this?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's karma for your evil deeds.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't play the victim.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing in particular.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What did you want, coming all the way to a place like this?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A thrilling adventure.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A treasure hunt.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Slaughter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What do ya usually eat?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Curry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>All sorts of things.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Protein.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What do you hope to accomplish by injuring me further...?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>More sleep.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Popularity.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There's no end if I start.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What do you think about humans showing pictures of their baby to others?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's cute.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not interested.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What has brought you to a place like this? What are you seeking?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>An adventure.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing, really.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>A killing spree.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What if I was a human? Then, what you're doing... Well, it'd be a criminal act!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's true...</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That can't be true.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's irrelevant.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What in the hell are ya tryin' ta tell me, anyway?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're going to die.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Why do we fight?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't really know...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What is irritating you so much?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Rotten adults.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Egotistical women.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm not irritated.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What kinda "fate" do you think there is in this meetin' between me and you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Fate brought us together.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>There is no such thing.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want to end this fate.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What kinda "hospitality" will you show me at the end of my life?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A homemade dinner.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A coupon for a massage by me.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll quietly be at your side.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What should I wear?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A Hight School Outfit.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>A Kimono.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't wear anything.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...What was that, anyway?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A love letter.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>A threat letter.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A coupon.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What was the cause of my defeat...?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Your lack of resolve.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My natural talent.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not telling.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What're you gonna tell your kids about this shit?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It was a hard-fought battle.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It was an easy win.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll forget it happened.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What's gonna happen to me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'll make mincemeat of you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll play nice.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll be your dominatrix.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">What's wrong with the way I look, huh?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You tempt people.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You're ugly.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing's wrong.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">When I was young, I could make anyone back off-if they were smart enough-with just my glare.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's so neat.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm just that good.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You've grown old.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">When it came down to it, you couldn't do anything to me!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I could.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>How could you tell?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What do you want me to do?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">When you eat curry, mister, what do you like to add?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Soy sauce.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Worcestershire sauce.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't add anything.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">When you were little, what did you wanna be when you grow up?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A pro athlete.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A famous celebrity.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>A winner in society.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Where do babies come from?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Storks deliver them.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Ask your parents.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>The love between two people.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Where should I go? I want something yummy, ho!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>A place with no wait.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A place with western toilets.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You won't survive.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...Who the blazes do you think you are?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I feel bad about that.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm ME!</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't owe you an answer.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="5">Why did you come to this dangerous place? Isn't it safer in the real world?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I've got business here.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm here for the loot.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just 'cause.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Why do they like "making out"?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>How should I know?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't tell you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Ask your parents.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Why have you decided to be more communicative with me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Your looks.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You seemed useful.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No particular reason.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Why you come all the way here?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>For a treasure hunt.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>For Girls.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I just felt like it.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Why you fight and put yourself in harm's way?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I want to get stronger.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Because I see an enemy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't actually know.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Why you keep trampling here? What you humans thinking?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm sorry.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Should I take off my shoes?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Why you not care for me like that? Why you treat me like this, then?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You look scary.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want to cherish you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're not a beast.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Why you wear mask to fight, anyway?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I care about my looks.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It keeps my foes' blood off.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's what I want to know.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Why're you so desperate?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I don't want to die.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There's something I must do.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I want the girls to like me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Won't you just leave me be?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Fine, I will.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I can't just leave you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Is that reverse psychology?</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Would you do to anyone what you're doing to me now?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I sure would.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I wouldn't.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This is a special exception.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Wouldn't your girlfriend get jealous if she could see us?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>No need to worry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's only bad if I get caught.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't have a girlfriend.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Y'know, if I'm gonna be killed, I'd rather be offed by a beautiful, classy lady.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Sorry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You don't get to be picky.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's all the same.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">Y'know what I'm gettin' at, right? Ya think ya could let me go see my girl?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Nope.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll consider it.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What kind of girl is she?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You better enjoy and be drunk on victory while you can. It not last long.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'll just keep winning.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're just a sore loser.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't drink, I'm underage.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You carry a gun because you think it'll make you more popular with the girls?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's right.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It won't?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's for self-improvement.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You didn't stray from the path or get lost?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I downloaded an app.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I took the train.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm with my friends!</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You do understand that we are here because of people like you, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I never thought of that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I understand</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>What do you mean?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You given much thought, what if you go to place where you could die at any moment?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I've thought about it.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't want kids.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm not comfortable with this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You go back to your mother's arms. You need take nap now.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm not that young.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not sleepy yet.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>After I'm done with this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You had something you lost, and you not know how important it was until after it gone, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>My pal who switched schools.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My ex-girlfriend...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Quiet, I'm killing you now.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You have wishes you not can let go of, even after you die?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Everyone's happiness.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>A grand funeral.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I won't die.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You, however are talking to me right here. Are you the exception to this rule?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm not special.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I have ulterior motives.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You knocked me down, and now my goddamn watch is broken!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>My apologies.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Like I care.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You should "watch" your mouth.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You know, a mascot's life isn't hee-easy. Are you sure you could handle all the adversity, ho?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm ready for it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What kind of adversity?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're a mascot?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You know, if I were to whip something up for you, what would you want?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Meat and potatoes.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't need homemade food.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Can you actually cook?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You know, if you're willin' to let this go... I'll make it worth your while.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Worth my while?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, thanks.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I already got enough, actually.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You must be one of those deliquents I hear about. Do you have poor grades in school?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm a straight-A student.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>They're not great...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>At least I'm popular.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You new? Did you get hee-hired, ho?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm a transfer student.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Yeah! Nice you meetcha!</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You not worry you get in trouble if those groups hear what you are doing to me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's true.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't mind.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's for love.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You, who reside in that world of the almighty, what is it that has beleaguered you so?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>The world is almighty?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not beleaguered.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My "dad" isn't almighty.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table>
	<tr>
		<th colspan="5">You will receive punishment for treating me this way, mark my words.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm sorry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm prepared for the worst.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>How much do you want?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You'd have no idea I was about to use my ultimate move.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>For real!?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That's worrying... </td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>...Try me.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You'll have a bleak future if you spend too much time running around pretending to be a phantom thief.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Thank you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't worry about it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's worth it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You'll probably break down in tears when you see my angry face. I'm a real monstrosity, ho!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's scary...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I would never cry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I want to see your fury.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You're a big bully! don't you think that's "immature"?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Now that you mention it...</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No, I don't think so.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not mature anyway.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You're hitting on me, right? Don't you think you're totally doing it wrong?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Nothing wrong about it.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What's the right way, then?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not hitting on you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You're lucky it was just me. You can't do anything like this in the real world, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I choose my targets carefully.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm serious about this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You're showing off your strength to me, aren't you? I total-hee read your mind, ho.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You're misunderstanding.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>The hell are you saying?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Make me your apprentice.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You're s'posed to go easy on kids! Are you stupid? Do you go to school and get stupid grades?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm smart.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm good at PE.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">You're violatin' the weapons code or whatever, man.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I didn't know.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's for self-defense.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Pretty cool, huh?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="X">
	<tr>
		<th colspan="5">...You've come from some other company to scout me-hee out. There's no mistaking it, ho!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>You got me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's a misunderstanding.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I've come to finish you off.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
</div>