<div style="display: none">If you are seeing this from Github, there is a user-friendly version of this page with an embeded searchbar at: http://joyce-chen.github.io/persona5-negotiation/<br><br>
</div>

<div style="display: flex; flex-wrap: wrap;">
	<div style="flex: 3" class="input-group">
		<input class="form-control py-2 border-right-0 border" type="text" id="searchBar" onkeyup="filterQuestions()" placeholder="Search for questions or responses.." title="Type in a question or response">
		<span class="input-group-append">
			<div class="input-group-text bg-transparent"><i class="fa fa-search"></i></div>
		</span>
	</div>

	<div style="flex: 1; text-align: center; margin-top: auto; margin-bottom: auto;">
		<label class="switch">
			<input type="checkbox" id="originalCompact" onClick="toggleOriginalCompact(false)">
			<span class="slider round">
				<i class="fas fa-icons"></i>
                <i class="fas fa-font"></i>
			</span>
		</label>
	</div>
</div>
<div style="margin-top: 1rem;">TIP: Reactions with a white background have been either sent in or are from my own playthrough; they are less likely to be wrong. Reactions that are empty or have a dash (-) are lacking data. Reactions with <span class="unconfirmed">pink backgrounds</span> are unconfirmed and are from the original game.
</div>

<div id="accordion" style="margin-top: 1rem;">
	<div class="card">
		<div class="card-header" style="padding: 0;">
			<a class="card-link" data-toggle="collapse" href="#shadowFilters" style="display: block; padding:.75rem 1.25rem">
			Filter Questions by Shadows (WIP feature)
			</a>
		</div>
		<div id="shadowFilters" class="collapse hide" data-parent="#accordion">
			<div class="card-body" id="shadowFilterBtns">
				<button class="btn filter-btn active" style="font-weight:bold;" onclick="filterByShadows('all')"> Show all</button>
				<button class="btn filter-btn" style="font-weight:bold;" onclick="filterByShadows('None')"> Uncategorized</button>
				<button class="btn filter-btn" onclick="filterByShadows('Agathion')"> Agathion</button>
				<button class="btn filter-btn" onclick="filterByShadows('Andras')"> Andras</button>
				<button class="btn filter-btn" onclick="filterByShadows('Angel')"> Angel</button>
				<button class="btn filter-btn" onclick="filterByShadows('Anubis')"> Anubis</button>
				<button class="btn filter-btn" onclick="filterByShadows('Anzu')"> Anzu</button>
				<button class="btn filter-btn" onclick="filterByShadows('Apsaras')"> Apsaras</button>
				<button class="btn filter-btn" onclick="filterByShadows('Arahabaki')"> Arahabaki</button>
				<button class="btn filter-btn" onclick="filterByShadows('Archangel')"> Archangel</button>
				<button class="btn filter-btn" onclick="filterByShadows('Baal')"> Baal</button>
				<button class="btn filter-btn" onclick="filterByShadows('Baphomet')"> Baphomet</button>
				<button class="btn filter-btn" onclick="filterByShadows('Barong')"> Barong</button>
				<button class="btn filter-btn" onclick="filterByShadows('Belphegor')"> Belphegor</button>
				<button class="btn filter-btn" onclick="filterByShadows('Berith')"> Berith</button>
				<button class="btn filter-btn" onclick="filterByShadows('Bicorn')"> Bicorn</button>
				<button class="btn filter-btn" onclick="filterByShadows('Black_Ooze')"> Black Ooze</button>
				<button class="btn filter-btn" onclick="filterByShadows('Cerberus')"> Cerberus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Chernobog')"> Chernobog</button>
				<button class="btn filter-btn" onclick="filterByShadows('Choronzon')"> Choronzon</button>
				<button class="btn filter-btn" onclick="filterByShadows('Dakini')"> Dakini</button>
				<button class="btn filter-btn" onclick="filterByShadows('Decarabia')"> Decarabia</button>
				<button class="btn filter-btn" onclick="filterByShadows('Dominion')"> Dominion</button>
				<button class="btn filter-btn" onclick="filterByShadows('Eligor')"> Eligor</button>
				<button class="btn filter-btn" onclick="filterByShadows('Forneus')"> Forneus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Fuu-ki')"> Fuu-ki</button>
				<button class="btn filter-btn" onclick="filterByShadows('Ganesha')"> Ganesha</button>
				<button class="btn filter-btn" onclick="filterByShadows('Garuda')"> Garuda</button>
				<button class="btn filter-btn" onclick="filterByShadows('Girimehkala')"> Girimehkala</button>
				<button class="btn filter-btn" onclick="filterByShadows('Hanuman')"> Hanuman</button>
				<button class="btn filter-btn" onclick="filterByShadows('High_Pixie')"> High Pixie</button>
				<button class="btn filter-btn" onclick="filterByShadows('Hua_Po')"> Hua Po</button>
				<button class="btn filter-btn" onclick="filterByShadows('Incubus')"> Incubus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Inugami')"> Inugami</button>
				<button class="btn filter-btn" onclick="filterByShadows('Ippon-Datara')"> Ippon-Datara</button>
				<button class="btn filter-btn" onclick="filterByShadows('Isis')"> Isis</button>
				<button class="btn filter-btn" onclick="filterByShadows('Jack_Frost')"> Jack Frost</button>
				<button class="btn filter-btn" onclick="filterByShadows('Jack-o-Lantern')"> Jack-o-Lantern</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kaiwan')"> Kaiwan</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kali')"> Kali</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kelpie')"> Kelpie</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kikuri-Hime')"> Kikuri-Hime</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kin-ki')"> Kin-ki</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kodama')"> Kodama</button>
				<button class="btn filter-btn" onclick="filterByShadows('Koppa_Tengu')"> Koppa Tengu</button>
				<button class="btn filter-btn" onclick="filterByShadows('Koropokguru')"> Koropokguru</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kumbhanda')"> Kumbhanda</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kushinada')"> Kushinada</button>
				<button class="btn filter-btn" onclick="filterByShadows('Lamia')"> Lamia</button>
				<button class="btn filter-btn" onclick="filterByShadows('Leanan_Sidhe')"> Leanan Sidhe</button>
				<button class="btn filter-btn" onclick="filterByShadows('Lilim')"> Lilim</button>
				<button class="btn filter-btn" onclick="filterByShadows('Lilith')"> Lilith</button>
				<button class="btn filter-btn" onclick="filterByShadows('Makami')"> Makami</button>
				<button class="btn filter-btn" onclick="filterByShadows('Mandrake')"> Mandrake</button>
				<button class="btn filter-btn" onclick="filterByShadows('Melchizedek')"> Melchizedek</button>
				<button class="btn filter-btn" onclick="filterByShadows('Mithras')"> Mithras</button>
				<button class="btn filter-btn" onclick="filterByShadows('Mokoi')"> Mokoi</button>
				<button class="btn filter-btn" onclick="filterByShadows('Moloch')"> Moloch</button>
				<button class="btn filter-btn" onclick="filterByShadows('Mot')"> Mot</button>
				<button class="btn filter-btn" onclick="filterByShadows('Mothman')"> Mothman</button>
				<button class="btn filter-btn" onclick="filterByShadows('Naga')"> Naga</button>
				<button class="btn filter-btn" onclick="filterByShadows('Narcissus')"> Narcissus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Nebiros')"> Nebiros</button>
				<button class="btn filter-btn" onclick="filterByShadows('Nekomata')"> Nekomata</button>
				<button class="btn filter-btn" onclick="filterByShadows('Norn')"> Norn</button>
				<button class="btn filter-btn" onclick="filterByShadows('Nue')"> Nue</button>
				<button class="btn filter-btn" onclick="filterByShadows('Obariyon')"> Obariyon</button>
				<button class="btn filter-btn" onclick="filterByShadows('Oberon')"> Oberon</button>
				<button class="btn filter-btn" onclick="filterByShadows('Oni')"> Oni</button>
				<button class="btn filter-btn" onclick="filterByShadows('Onmoraki')"> Onmoraki</button>
				<button class="btn filter-btn" onclick="filterByShadows('Orobas')"> Orobas</button>
				<button class="btn filter-btn" onclick="filterByShadows('Orthrus')"> Orthrus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Ose')"> Ose</button>
				<button class="btn filter-btn" onclick="filterByShadows('Parvati')"> Parvati</button>
				<button class="btn filter-btn" onclick="filterByShadows('Pisaca')"> Pisaca</button>
				<button class="btn filter-btn" onclick="filterByShadows('Pixie')"> Pixie</button>
				<button class="btn filter-btn" onclick="filterByShadows('Power')"> Power</button>
				<button class="btn filter-btn" onclick="filterByShadows('Queen_Mab')"> Queen Mab</button>
				<button class="btn filter-btn" onclick="filterByShadows('Rakshasa')"> Rakshasa</button>
				<button class="btn filter-btn" onclick="filterByShadows('Rangda')"> Rangda</button>
				<button class="btn filter-btn" onclick="filterByShadows('Sandman')"> Sandman</button>
				<button class="btn filter-btn" onclick="filterByShadows('Sarasvati')"> Sarasvati</button>
				<button class="btn filter-btn" onclick="filterByShadows('Scathach')"> Scathach</button>
				<button class="btn filter-btn" onclick="filterByShadows('Shiki-Ouji')"> Shiki-Ouji</button>
				<button class="btn filter-btn" onclick="filterByShadows('Silky')"> Silky</button>
				<button class="btn filter-btn" onclick="filterByShadows('Skadi')"> Skadi</button>
				<button class="btn filter-btn" onclick="filterByShadows('Slime')"> Slime</button>
				<button class="btn filter-btn" onclick="filterByShadows('Succubus')"> Succubus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Sudama')"> Sudama</button>
				<button class="btn filter-btn" onclick="filterByShadows('Sui-ki')"> Sui-ki</button>
				<button class="btn filter-btn" onclick="filterByShadows('Take-Minakata')"> Take-Minakata</button>
				<button class="btn filter-btn" onclick="filterByShadows('Thor')"> Thor</button>
				<button class="btn filter-btn" onclick="filterByShadows('Thoth')"> Thoth</button>
				<button class="btn filter-btn" onclick="filterByShadows('Titania')"> Titania</button>
				<button class="btn filter-btn" onclick="filterByShadows('Unicorn')"> Unicorn</button>
				<button class="btn filter-btn" onclick="filterByShadows('Valkyrie')"> Valkyrie</button>
				<button class="btn filter-btn" onclick="filterByShadows('Yaksini')"> Yaksini</button>
				<button class="btn filter-btn" onclick="filterByShadows('Yamata-no-Orochi')"> Yamata-no-Orochi</button>
			</div>
		</div>
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

function toggleOriginalCompact(loading) {
	var compactSwitch = document.getElementById("originalCompact");
	if (!loading) {
		localStorage.setItem(compactSwitch.id, compactSwitch.checked);
	}
	var checked = JSON.parse(localStorage.getItem(compactSwitch.id));

	var text = document.getElementsByClassName("text");
	var symbol = document.getElementsByClassName("symbol");
	for (var i = 0; i < text.length; i++) {
		if (checked) {
			symbol[i].style.display = "block";
			text[i].style.display = "none";
		} else {
			symbol[i].style.display = "none";
			text[i].style.display = "block";
		}
	}

	var extra = document.getElementsByClassName("extra");
	for (var i = 0; i < extra.length; i++) {
		if (checked) {
			extra[i].style.display = "none";
		} else {
			extra[i].style.display = "inline";
		}
	}
}

function filterByShadows(shadow) {
	var target = document.getElementsByClassName("filterDiv");
	if (shadow == "all") shadow = "";
	for (var i = 0; i < target.length; i++) {
		filterAddClass(target[i], "hidden");
		if (target[i].className.indexOf(shadow) > -1) {
			filterRemoveClass(target[i], "hidden");
		}
	}
}

function filterAddClass(element, name) {
	var arr1 = element.className.split(" ");
	var arr2 = name.split(" ");
	for (var i = 0; i < arr2.length; i++) {
		if (arr1.indexOf(arr2[i]) == -1) {
			element.className += " " + arr2[i];
		}
	}
}

function filterRemoveClass(element, name) {
	var arr1 = element.className.split(" ");
	var arr2 = name.split(" ");
	for (var i = 0; i < arr2.length; i++) {
		while (arr1.indexOf(arr2[i]) > -1) {
			arr1.splice(arr1.indexOf(arr2[i]), 1);     
		}
	}
	element.className = arr1.join(" ");
}

var btnContainer = document.getElementById("shadowFilterBtns");
var btns = btnContainer.getElementsByClassName("btn filter-btn");
for (var i = 0; i < btns.length; i++) {
	btns[i].addEventListener("click", function(){
		var current = document.getElementsByClassName("btn filter-btn active");
		current[0].className = current[0].className.replace(" active", "");
		this.className += " active";
	});
}
</script>

<div id="questions">
<table class="filterDiv Baphomet Chernobog Bicorn Berith Koropokguru Oni Anubis Belphegor Forneus Ippon-Datara Fuu-ki">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't know any other way.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Skadi">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You've got a point...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What's wrong with that?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Barong Chernobog Mithras Naga Mokoi">
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
		<td>Then get serious now.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Making excuses?</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I wasn't trying either.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Apsaras High_Pixie Isis Lamia Scathach Queen_Mab Parvati Titania">
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
		<td>That's not true.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Age doesn't matter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This isn't extreme.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Oberon Naga">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't stop.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll find meaning in it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Oni Belphegor Choronzon Koropokguru Kumbhanda Bicorn Eligor Ippon-Datara Anubis Oni">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I thought this up myself.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Want to join in?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Lilim Mandrake Succubus Angel">
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
		<td>A thrift shop.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Internet shopping.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Obariyon Agathion Onmoraki">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Agathion">
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
		<td>That's right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Obariyon Kodama Agathion Onmoraki Sudama">
	<tr>
		<th colspan="5">Aren't people as old as you s'posed to go "dating," all the time? Can't you get some dates?</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Such a rude little boy...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Dating's not important.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Barong Baal Naga Mithras">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Nobody, really.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It doesn't matter.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv None">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv High_Pixie Silky Isis Lamia Parvati Sarasvati">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rangda Skadi Kali">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I just want you to die happy.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv None">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Hee-haw!</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Personaaa!</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Naga Mithras Mokoi Baal">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Green.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I never bleed or cry.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Power">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Apsaras Titania Silky High_Pixie Leanan_Sidhe Isis Lamia Scathach Valkyrie Queen_Mab Sarasvati">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>There's no need to explain.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just shut up.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Power">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Yaksini">
	<tr>
		<th colspan="5">Could this be what you humans call a proposal?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I’m surprised you knew.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, it’s not.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That’s a myth.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Bicorn Berith Koropokguru Oni Anubis Belphegor Chernobog Ippon-Datara Choronzon Fuu-ki">
	<tr>
		<th colspan="5">Couldn't you at least make me a cup of tea or somethin'? Hell, that'd be real polite.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I don't have any.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Brew your own.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not hospitable.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm a little scared...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Shut up!</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Incubus Koppa_Tengu Rakshasa Sandman Black_Ooze Kaiwan Girimehkala Ose Sui-ki Mot">
	<tr>
		<th colspan="5">Did I lose... ?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I suppose so...</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What don't you get?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nah, you totally won.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Agathion Onmoraki Kodama">
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
		<td>Being a kid is easy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Being a kid is tough.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't remember.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Yaksini Hua_Po Nekomata Kushinada">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Spaghetti carbonara.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What are you saying?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Lilim Mandrake Succubus Angel">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Power">
	<tr>
		<th colspan="5">Do you not understand the severity of your action?</th>
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
		<td>Cut to the chase.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I've done nothing wrong.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Power Dominion Archangel">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're a loathsome foe.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Sudama Agathion Obariyon Onmoraki">
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
		<td>Yes.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, but they say it anyway.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm cuter than most kids.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Oberon Mokoi Naga">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>...Nope</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm past such things.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Ippon-Datara Berith Koropokguru Anubis Belphegor Kumbhanda Decarabia">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I prefer being an adult.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I wish I was still a baby.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Parvati Silky Apsaras Leanan_Sidhe Lamia Queen_Mab Valkyrie">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't think its unfair.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't fret about it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Dakini">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Agathion Obariyon Kodama Onmoraki">
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
		<td>I'm not your dad.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Ask someone else.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll make your sleep eternal.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern Jack_Frost">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's not it.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Archangel Power Dominion">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's absurd.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Incubus Mot Koppa_Tengu Orobas Rakshasa Sandman Black_Ooze Girimehkala Ose">
	<tr>
		<th colspan="5">Hell, I got all sorta girls lined up if you're into that.</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're trying way too hard.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm not interested.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Mandrake Angel Lilim">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>If we split the cost.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm on a diet.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Mandrake Lilim">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Bicorn Berith Koropokguru Anubis Kumbhanda Ippon-Datara Eligor Belphegor">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That won't change anything?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Succubus Angel Lilim Mandrake">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Who cares?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Agathion Sudama Kodama Onmoraki">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Curry.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
<table class="filterDiv Mandrake Lilim Pixie Angel Succubus">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>A weathly housewife.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Living in the darkness.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Obariyon Sudama Kodama Onmoraki">
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
		<td>No.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't eat between meals.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Decarabia Chernobog Ippon-Datara Hanuman Belphegor Anubis Oni Koropokguru Eligor">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Live fast, die young.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I just want to enjoy the now.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Berith Koropokguru Kumbhanda Choronzon">
	<tr>
		<th colspan="5">Hey, sonny if somethin's been botherin' you. I'm willing to give you a listen.</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My future...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I have no worries.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Yaksini Nekomata Kushinada">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Bicorn Ippon-Datara Hanuman Kumbhanda Decarabia Belphegor Anubis Oni Koropokguru Berith">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't feel like going.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I actually finished school.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Lilim Succubus">
	<tr>
		<th colspan="5">Honestly, aren't I, like, a way better girl than those idols?</th>
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Sandman Kaiwan Girimehkala">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want to aim higher.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Fighting is pointless.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Bicorn Berith Koropokguru Anubis Decarabia Fuu-ki Thor">
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
		<td>A hitchhiking adventure.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>A trip to hell.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Girimehkala Rakshasa Black_Ooze Sandman">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's impossible.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Now that you mention it...</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>...Cute?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern Jack_Frost">
	<tr>
		<th colspan="5">How did I lose to you? I mean... I win when it comes to looks, ho.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I worked hard.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I do.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's all about heart.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern Jack_Frost">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A speciatly site.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Word of mouth.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern Jack_Frost">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want a photo.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Give me your credit card.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Belphegor Berith Oni Anubis Eligor">
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
		<td>Quit messing around.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You'll really treat me?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm a minor...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Silky High_Pixie Isis Lamia Valkyrie">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>None of your business.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm always alone.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
<table class="filterDiv Incubus Koppa_Tengu Take-Minakata Orobas Rakshasa Sandman Black_Ooze Kaiwan Girimehkala Sui-ki">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That's never happening.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Are you giving up?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon">
	<tr>
		<th colspan="5">I don't hate you. No, I don't feel that way at all...</th>
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Too late.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Archangel Power">
	<tr>
		<th colspan="5">I fear neither death... nor you.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Why are you telling me this?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's a lie.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Quit acting tough.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Baphomet Bicorn Koropokguru Ippon-Datara Hanuman Decarabia Belphegor Oni Berith Chernobog">
	<tr>
		<th colspan="5">...I gotta ask. How do you train?</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I just have a knack for it.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Luck's usually on my side.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Apsaras Leanan_Sidhe Silky High_Pixie Isis Lamia Scathach Valkyrie Kikuri-Hime">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't have the time.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You've got the wrong idea.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Pisaca Girimehkala Ose Ganesha Kaiwan Rakshasa Orobas Take-Minakata Koppa_Tengu">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Not at all.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Why does that matter?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Nekomata Yaksini">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Grovel before me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't know.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Narcissus Mithras Naga Baal">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>...I could get used to it.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It pains my heart...</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Silky Parvati Queen_Mab Scathach Isis">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Go impulse shopping.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Don't be so selfish.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rangda">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It can't be helped.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Apsaras Titania Silky Queen_Mab Scathach Lamia Leanan_Sidhe High_Pixie Sarasvati">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm always so busy there.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's better than here.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv None">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Being alone is a luxury.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Agathion Kodama Obariyon">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's because you're cute.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Nekomata Yaksini">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You have a boyfriend?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv None">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="filterDiv Skadi Rangda">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There's an aging boom...</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Yaksini Nekomata">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Sarasvati Titania Silky Apsaras High_Pixie Leanan_Sidhe Lamia Norn Kikuri-Hime Valkyrie Queen_Mab Parvati">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I don't think so.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's what we call destiny.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Mokoi Naga Mithras">
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
		<td>What a pity...</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Uninformed choices are bad.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Complaining won't help.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Naga Oberon Mithras Mokoi">
	<tr>
		<th colspan="5">If I'd known things would end like this, I wish I had found the courage to ask that girl out...</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Too late for regrets.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You never had a chance.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll make "that girl" happy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Baal Mokoi Naga">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>A deal with the enemy?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't trust you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Nekomata Yaksini">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't understand.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What would you like?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Succubus Angel">
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
		<td>Don't be ridiculous.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Ippon-Datara Bicorn Berith Oni Anubis Belphegor Hanuman Kumbhanda">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll have more fun first.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Stop trying to act cool.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oni Bicorn Koropokguru Anubis Ippon-Datara Chernobog Kumbhanda Decarabia Belphegor">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's not very fun.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Kin-ki Kelpie Andras Inugami Nue Shiki-Ouji Orthrus Anzu Mothman Unicorn">
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
		<td>Eat you in a hot pot.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Take you to a taxidermist.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You'll be my new stylish coat.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Yaksini Hua_Po Nekomata">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm busy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Chernobog Naga">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This doesn't involve them.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Actually, they'd rejoice.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Succubus">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No strings attached?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I've got enough on my plate...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Complicated...?</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Liar.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack_Frost">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Fans?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Apsaras Lamia Titania Silky Sarasvati Parvati Valkyrie Norn Scathach Isis High_Pixie Leanan_Sidhe">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD / BAD ?</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Are you bored?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That's horrible premise.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Nekomata Yaksini">
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
		<td>That's not it at all.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You look young.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Cougars are all the rage now.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Silky Apsaras High_Pixie Leanan_Sidhe Isis Lamia Queen_Mab Scathach">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Prepare for the worst.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>How much do you want?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Oberon Mithras Naga Mokoi">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's absurd.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Anyone will do.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Incubus Black_Ooze Girimehkala">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'd be jealous if it did.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm waiting.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Succubus Angel Lilim">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No one bothers me.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I hate everyone.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Agathion Obariyon Kodama Onmoraki">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Bicorn Anubis">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Enemies must be eliminated.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Koropokguru Choronzon Bicorn Berith Anubis Decarabia Kumbhanda Fuu-ki Belphegor">
	<tr>
		<th colspan="5">In the very end, what the hell are you tryin' ta tell me?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'm telling you to die.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Why do we fight?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't really know...</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Angel Mandrake">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Paying your own rent.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Questioning maturity.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Obariyon Agathion Onmoraki Sudama Kodama">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That's not why.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Queen_Mab Leanan_Sidhe Silky Apsaras Isis Lamia">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That is incorrect.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Agathion Onmoraki">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I endure it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I like shots.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Nekomata Yaksini Kushinada">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Figure it out yourself.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Silky Leanan_Sidhe Isis Lamia Kikuri-Hime Queen_Mab High_Pixie">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I can't promise that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's a matter of feeling.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rangda Kali Dakini">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I love someone else.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Power Archangel">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I feel his gaze.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Orthrus Anzu Nue Yamata-no-Orochi">
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
		<td>It doesn't change the facts.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I never tell lies.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't try to escape reality.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Ganesha Girimehkala Kaiwan Koppa_Tengu Take-Minakata Orobas Rakshasa Sandman Black_Ooze Ose">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I had no idea.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This'll be your deathday too.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Oberon Mithras Naga Mokoi">
	<tr>
		<th colspan="5">It's cliched, but we could chat about life... Ask each other things like what kind of girls we like...</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I like younger women.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I like men.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Mokoi Naga Mithras Narcissus">
	<tr>
		<th colspan="5">...It's fine. Do as you please.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Give me everything you got.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Mandrake Succubus Angel Lilim">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, not all.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I look ok, I guess.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Pixie Mandrake Succubus Angel Lilim">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You should love your parents.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Make sure you go home.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Incubus Koppa_Tengu Take-Minakata Rakshasa Sandman Kaiwan Girimehkala Ose Orobas Black_Ooze">
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
		<td>Nope.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's part of my face.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Try and rip it off me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Lamia Silky Valkyrie Leanan_Sidhe Apsaras Sarasvati Isis">
	<tr>
		<th colspan="5">I've been sending you serious "don't speak to me" vibes.</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I didn't see any "vibes."</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>But we may never meet again...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Yaksini">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Definitely not.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What are you saying?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rakshasa Black_Ooze Girimehkala Incubus">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I never thought about it.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I prefer mutual respect.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Bicorn Koropokguru Chernobog">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't want to grow old.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Take-Minakata Sandman Black_Ooze Girimehkala Koppa_Tengu">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You won't die easily.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Bicorn Berith Anubis">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Don't expect it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>The elderly have bad manners.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Angel Lilim Mandrake">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Please don't.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It was self-defense.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Obariyon Onmoraki">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Slime Arahabaki Anzu Shiki-Ouji Nue Makami Andras Orthrus Thoth">
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
		<td>OK, I'll make you into soup.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Fine I'll grill you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>All right I'll mince you!</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Slime Mothman Arahabaki Thoth Anzu Orthrus Shiki-Ouji Makami Inugami Yamata-no-Orochi">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's money.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Girl power.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Slime Arahabaki Thoth Anzu Nue Andras">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Fighting me is bad luck.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Just try to escape.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Andras Inugami Nue Orthrus Anzu Thoth Arahabaki Unicorn Kin-ki">
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
		<td>I'm younger than you.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm cuter than you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm better at small talk.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Kin-ki Arahabaki Andras Inugami Makami Nue Orthrus Anzu Thoth Mothman Unicorn">
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
		<td>Don't joke around.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just endure it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Want something delivered?</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Inugami Arahabaki Slime">
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
		<td>Bread dipped in coffee.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Ice cream off the carton lid.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Hunger is the best spice.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Thoth Slime">
	<tr>
		<th colspan="5">Me want you to give me some nice "words of compassion"-as my rival-as me pass away...!</th>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Angel Mandrake Lilim">
	<tr>
		<th colspan="5">My horoscope said I was going to have relationship troubles today.</th>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>What are your plans?</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You had a good run...</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv None">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Rangda Dakini">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Mandrake Succubus Angel">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Archangel Power">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Incubus Kaiwan Black_Ooze Sandman Rakshasa Take-Minakata Koppa_Tengu Ganesha Ose Girimehkala">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I'm actually very busy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Kodama Obariyon">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Yaksini Lilith">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're fine as you are.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's pointless.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Shiki-Ouji Makami">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I could carry that weight.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I wouldn't like that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Black_Ooze Incubus Koppa_Tengu Sandman Kaiwan Girimehkala Ganesha Rakshasa">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No... Nothing at all...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're too self-conscious.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Nekomata Yaksini">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What do you want to happen?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's a secret.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Incubus Sui-ki Ose Kaiwan Black_Ooze Sandman Rakshasa Koppa_Tengu Girimehkala">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Shuddup...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm actually still young...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Makami Kelpie Slime Mothman Arahabaki Anzu Shiki-Ouji Nue Inugami Andras">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Humans are powerful.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>This is a difficult topic...</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Yaksini Kushinada Lilith">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It is fun, actually.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm serious.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rangda">
	<tr>
		<th colspan="5">Some old people refuse to make use of special seats reserved for the elderly. What do you think of that?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>No problem with it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>They shouldn't push themselves.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>They must be young inside.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Bicorn Berith Koropokguru Decarabia Ippon-Datara Choronzon Fuu-ki Oni Kumbhanda Belphegor Anubis">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing but bad things...</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're getting on my nerves!</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Rangda Skadi">
	<tr>
		<th colspan="5">Something about people putting honey on cucumbers to feel like they're eating fancy cantaloupe...?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I use those tips.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It makes me sad.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Finding new tricks is fun.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="filterDiv Silky Sarasvati Valkyrie Lamia Isis Scathach">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I didn't think that far.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>The feelings will come.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kikuri-Hime Silky Isis Lamia Valkyrie Scathach Leanan_Sidhe">
	<tr>
		<th colspan="5">Tell me, what does "equality" mean to you?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Lamia Titania Silky Queen_Mab Valkyrie Norn Scathach Leanan_Sidhe High_Pixie">
	<tr>
		<th colspan="5">That may be because my life may also be meaningless. All I've known is the way of life here.</th>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>There are other ways to live.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You had a good run.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Power Archangel">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This is my power.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Archangel Dominion Power">
	<tr>
		<th colspan="5">That power, vow that you will use it in the name of our Father.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I'll consider it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's a bit much.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I refuse.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Apsaras Isis Lamia">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Incubus Take-Minakata Rakshasa Sandman Ganesha Koppa_Tengu Girimehkala">
	<tr>
		<th colspan="5">That's wack, man. Maybe you should get your head checked out.</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm fine as is.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're a sore loser.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Dominion Power Archangel">
	<tr>
		<th colspan="5">...The least I can do is extend this small mercy. Confess the calamity that you can bear.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Stores are always so crowded.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I always manage to step in gum.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK/GOOD?</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I won't confess anything.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Mithras Oberon Naga Mokoi Nebiros">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Actually... I'm bad.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Are you mocking me?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Yaksini Hua_Po Kushinada">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're scary.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing in particular.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Andras Inugami Makami Nue Shiki-Ouji Orthrus Anzu Thoth Arahabaki Cerberus Slime Take-Minakata Kelpie Mothman">
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
		<td>Don't scratch the furniture.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll housebreak you.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Let me touch your paws.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Power Melchizedek">
	<tr>
		<th colspan="5">Therefore, I cannot be destroyed. Desist from this pointlessness.</th>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's absurd.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're lying.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Incubus Sui-ki Ose Sandman Rakshasa Orobas Koppa_Tengu Black_Ooze">
	<tr>
		<th colspan="5">They always give the guys katsudon! You got anything like that for me!?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>How about sushi...?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I have nothing for you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Skadi Rangda">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern Jack_Frost">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>What's all this now?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>This is real.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Agathion Obariyon Onmoraki Kodama Sudama">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack_Frost">
	<tr>
		<th colspan="5">To tell you the hee-truth, this is all an act, ho. What do you think I'm really like, ho?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I can't imagine it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't care.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're fine as is.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Power Archangel">
	<tr>
		<th colspan="5">To view me as an enemy is to incur our Father's wrath. Man's future rests in your hands.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>What are you trying to say?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're exaggerating.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's pretty complicated.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Yaksini">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Should I go instead?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
<table class="filterDiv Incubus Black_Ooze Girimehkala">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's coming from you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I smell a lie.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Incubus Ose Ganesha Girimehkala Kaiwan Sandman Rakshasa Orobas Take-Minakata">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Loud talkers...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Nobody.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Archangel">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Taxes keep going up.</td>
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
<table class="filterDiv Yaksini Hua_Po">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What do you mean?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't lie to me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv None">
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
<table class="filterDiv Mandrake Succubus Lilim">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't agree with this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>We can say you won.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rangda Skadi Dakini">
	<tr>
		<th colspan="5">Well, quite frankly... No one wants you here. You do understand that, right?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I know.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I didn't know that.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Who cares?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Agathion Sudama Onmoraki">
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
		<td>Let's play tag.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Let's play a video game.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Let's hit on some ladies.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Chernobog Mokoi Mithras">
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
		<td>You're kind of evil.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't play the tragic hero.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You were born.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Mithras Naga Mokoi">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A treasure hunt.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Slaughter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Baphomet Bicorn Choronzon Ippon-Datara Forneus Belphegor Anubis Oni Koropokguru">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Vegetables.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Archangel">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Popularity.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There's no end if I start.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Nekomata Yaksini">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Pixie Lilim Angel">
	<tr>
		<th colspan="5">What do you think I should wear? I admit it, I wanna draw some attention to myself</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>High school uniform</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Kimono</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don’t wear anything</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Oberon Chernobog Mithras Naga Mokoi">
	<tr>
		<th colspan="5">What if I was a "human"? Then, what you're doing... Well, it'd be a criminal act!</th>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That can't be true.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>That's unrelated.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Leanan_Sidhe Silky Titania Sarasvati Parvati Queen_Mab Valkyrie Kikuri-Hime Scathach Lamia Isis High_Pixie Apsaras">
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
		<td>Slow-ass cashiers.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Egotistical women.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not irritated.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Yaksini">
	<tr>
		<th colspan="5">What kind of place do you want to live in?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Close to a train station.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Next to a convenience store.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
<table class="filterDiv Berith Koropokguru Oni Belphegor Kumbhanda Hanuman">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>There is no such thing.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want to end this fate.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Bicorn">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A coupon for a massage by me.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll quietly be at your side.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Mandrake">
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
		<td>A High School Outfit.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Onmoraki Agathion Sudama">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A threat letter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A coupon.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Mokoi Naga">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My natural talent.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm not telling.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Nue Kelpie Cerberus Andras Inugami Makami Nue Orthrus Anzu Thoth Arahabaki Mothman Slime Garuda">
	<tr>
		<th colspan="5">What you thinking now?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I have homework tonight.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I need a new cell phone.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want girls to like me.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Rakshasa">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Girimehkala Rakshasa Kaiwan">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Moloch Ippon-Datara Bicorn Berith Choronzon Hanuman Belphegor Oni">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You're ugly.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing's wrong.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Rangda Skadi">
	<tr>
		<th colspan="5">When I was young, I could make anyone back off - if they were smart enough - with just my glare.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Fights are just luck.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm just that good.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="filterDiv Agathion Obariyon Kodama Onmoraki">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Worcestershire sauce.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't add anything.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Sudama Onmoraki Kodama Agathion Obariyon">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A famous celebrity.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>A winner in society.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Obariyon Sudama Onmoraki Kodama">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Ask your parents.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>The love between two people.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A place with western toilets.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You won't survive.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Barong Oberon Chernobog Mithras Naga Mokoi">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm ME!</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD / BAD ?</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't have to answer you.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rangda">
	<tr>
		<th colspan="5">Why did you come to such a dangerous place? Isn't it much safer in the real world?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>There are things I must do.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm just too curious.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>The real world is oppressive.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Agathion Obariyon Onmoraki Sudama">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Ask your parents.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Lamia Silky High_Pixie Leanan_Sidhe Isis Valkyrie Queen_Mab Parvati">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You seemed useful.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No particular reason.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kin-ki Kelpie Slime Cerberus Unicorn Mothman Thoth Anzu Orthrus Shiki-Ouji Nue Makami Inugami Andras Arahabaki">
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
		<td>I'm here for the food.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm here for the women.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm here to find myself.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Andras Inugami Nue Shiki-Ouji Orthrus Anzu Thoth Arahabaki Slime Yamata-no-Orochi">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Because I see an enemy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't actually know.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Mothman Kelpie Slime Arahabaki Thoth Anzu Orthrus Nue Makami Inugami">
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
		<td>Sorry about that.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I haven't thought about it.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Ugh, you talk too loud.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Cerberus Kelpie Slime Unicorn Thoth Nue Makami Inugami">
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
		<td>You look terrifying.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't play with you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're not an animal.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Andras Kelpie Unicorn Arahabaki Thoth Anzu Shiki-Ouji Makami Nue Inugami Orthrus">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It keeps my foes' blood off.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's what I want to know.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Incubus Sui-ki Ose Ganesha Girimehkala Kaiwan Sandman Rakshasa Take-Minakata Orobas Koppa_Tengu">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There's something I must do.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I'm not desperate.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="filterDiv Apsaras Silky High_Pixie Isis Lamia Scathach Norn Queen_Mab Sarasvati Leanan_Sidhe">
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
		<td>Are you busy?</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I just couldn't.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Is that reverse psychology?</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Skadi">
	<tr>
		<th colspan="5">Would you be willing to spend time and money to see people you haven't contacted for years?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Maybe, I guess.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Sounds like a drag.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It'd be too awkward.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Norn Scathach High_Pixie Sarasvati Silky Parvati Queen_Mab Lamia Leanan_Sidhe Apsaras Valkyrie">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD / BAD ?</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I wouldn't.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This is a special exception.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Yaksini Kushinada">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't have a girlfriend.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Berith Koropokguru Kumbhanda Ippon-Datara Eligor Fuu-ki Bicorn Belphegor">
	<tr>
		<th colspan="5">Y'know, if I'm gonna be killed, I'd rather be offed by some beautiful, classy woman.</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You don't get to be picky.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's all the same.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Nue">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're just a sore loser.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't drink, I'm underage.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Angel Lilim Succubus Mandrake">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It won't?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>It's for self-improvement.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon Mithras Naga Mokoi">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I took the train.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm with my friends!</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Oberon">
	<tr>
		<th colspan="5">You do know that just pointing that at someone doesn't actually do anything, right? Buffoon.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I know.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't act so tough.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're doing nothing, too.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Silky Apsaras Leanan_Sidhe Lamia Parvati">
	<tr>
		<th colspan="5">You do understand that I'm here because people like you exist, right?</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Eh, doesn't matter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>What do you mean?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Slime Mothman Arahabaki Thoth Anzu Orthrus Shiki-Ouji Nue Makami">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't want kids.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm not comfortable with this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Slime Cerberus Arahabaki Thoth Anzu Orthrus Shiki-Ouji Nue Makami Inugami Mothman">
	<tr>
		<th colspan="5">You go back to your mother' arms. You need take nap now.</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not sleepy yet.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Mom will wait till I'm done.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Arahabaki Slime Thoth">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My ex-girlfriend...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Quiet, I'm killing you now.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kaiwan Incubus Sui-ki Ganesha Girimehkala Sandman Rakshasa Orobas Take-Minakata Koppa_Tengu">
	<tr>
		<th colspan="5">You have no idea I was about to use my ultimate move.</th>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That's worrying... </td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>...Try me.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Makami Anzu Mothman Unicorn">
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
		<td>Yes, I want world peace.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I want a grand funeral.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't plan on dying.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Silky Apsaras High_Pixie Isis">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I have ulterior motives.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Koppa_Tengu Take-Minakata Rakshasa Ose Mot Girimehkala">
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
		<td>Sorry...</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Not my problem.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Don't lie.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern Jack_Frost">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What kind of adversity?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="filterDiv Lilith Hua_Po Nekomata Yaksini">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't need homemade food.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Can you actually cook?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Hua_Po Nekomata Yaksini">
	<tr>
		<th colspan="5">You know... If you're willin' to let this go... I'll make it worth your while.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Worth my while...?</td>
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
		<td>I'm already taken.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Berith Choronzon Ippon-Datara Kumbhanda Belphegor Koropokguru Anubis">
	<tr>
		<th colspan="5">...You know what I'm getting' at, right? You think you could let me go see my girl?</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>She probably left.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What kind of girl is she?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Skadi Rangda">
	<tr>
		<th colspan="5">You must be one of those delinquents I hear about. Do you have poor grades in school?</th>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>At least I'm popular.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Kelpie Slime Unicorn Mothman Arahabaki Thoth Anzu Orthrus Shiki-Ouji Makami Inugami Andras">
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
		<td>You're right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're not an animal.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rangda Skadi Dakini">
	<tr>
		<th colspan="5">You were so sure of yourself it's embarrassing now to admit you're struggling here? Right?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't make fun of me.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Power Dominion">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My "dad" isn't almighty.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Rangda">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>None of your business.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's worth it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern Jack_Frost">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I would never cry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I want to see your fury.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="filterDiv Obariyon Agathion Onmoraki Sudama Kodama">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Succubus Lilim Mandrake">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What's the right way, then?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="filterDiv Angel Succubus">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I choose my targets carefully.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="filterDiv Jack-o-Lantern Jack_Frost">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Obariyon Agathion Sudama Kodama Onmoraki">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My grades are all right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="filterDiv Girimehkala Kaiwan Sui-ki Ose Ganesha Black_Ooze Rakshasa Take-Minakata Koppa_Tengu Sandman">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Not if no one finds out.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Pretty cool, huh?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="filterDiv Jack-o-Lantern">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's a misunderstanding.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I've come to finish you off.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="filterDiv Dakini">
	<tr>
		<th colspan="5">I guess women are really more social these days, finding so many fun things to do outside.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's the women's fault.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Men are social too.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Is that so?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
</div>

<!-- LOCAL STORAGE OF SWITCH STATE -->
<script>
window.onload = onPageLoad();

function onPageLoad() {
	var switchState = JSON.parse(localStorage["originalCompact"] || false);
	var compactSwitch = document.getElementById("originalCompact");
	if (switchState) {
		compactSwitch.checked = true;
		toggleOriginalCompact(true);
	}
}
</script>