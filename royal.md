<div style="display: none">If you are seeing this from Github, there is a user-friendly version of this page with an embeded searchbar at: http://joyce-chen.github.io/persona5-negotiation/royal<br><br>
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
			<input type="checkbox" id="royalCompact" onClick="toggleRoyalCompact(false)">
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
				<button class="btn filter-btn" onclick="filterByShadows('Abaddon')"> Abaddon</button>
				<button class="btn filter-btn" onclick="filterByShadows('Agathion')"> Agathion</button>
				<button class="btn filter-btn" onclick="filterByShadows('Alilat')"> Alilat</button>
				<button class="btn filter-btn" onclick="filterByShadows('Ame-no-Uzume')"> Ame-no-Uzume</button>
				<button class="btn filter-btn" onclick="filterByShadows('Andras')"> Andras</button>
				<button class="btn filter-btn" onclick="filterByShadows('Angel')"> Angel</button>
				<button class="btn filter-btn" onclick="filterByShadows('Anubis')"> Anubis</button>
				<button class="btn filter-btn" onclick="filterByShadows('Anzu')"> Anzu</button>
				<button class="btn filter-btn" onclick="filterByShadows('Apsaras')"> Apsaras</button>
				<button class="btn filter-btn" onclick="filterByShadows('Arahabaki')"> Arahabaki</button>
				<button class="btn filter-btn" onclick="filterByShadows('Archangel')"> Archangel</button>
				<button class="btn filter-btn" onclick="filterByShadows('Atavaka')"> Atavaka</button>
				<button class="btn filter-btn" onclick="filterByShadows('Baal')"> Baal</button>
				<button class="btn filter-btn" onclick="filterByShadows('Baphomet')"> Baphomet</button>
				<button class="btn filter-btn" onclick="filterByShadows('Barong')"> Barong</button>
				<button class="btn filter-btn" onclick="filterByShadows('Belphegor')"> Belphegor</button>
				<button class="btn filter-btn" onclick="filterByShadows('Berith')"> Berith</button>
				<button class="btn filter-btn" onclick="filterByShadows('Bicorn')"> Bicorn</button>
				<button class="btn filter-btn" onclick="filterByShadows('Black_Ooze')"> Black Ooze</button>
				<button class="btn filter-btn" onclick="filterByShadows('Byakhee')"> Byakhee</button>
				<button class="btn filter-btn" onclick="filterByShadows('Cait_Sith')"> Cait Sith</button>
				<button class="btn filter-btn" onclick="filterByShadows('Cerberus')"> Cerberus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Chernobog')"> Chernobog</button>
				<button class="btn filter-btn" onclick="filterByShadows('Chimera')"> Chimera</button>
				<button class="btn filter-btn" onclick="filterByShadows('Choronzon')"> Choronzon</button>
				<button class="btn filter-btn" onclick="filterByShadows('Cu_Chulainn')"> Cu Chulainn</button>
				<button class="btn filter-btn" onclick="filterByShadows('Dakini')"> Dakini</button>
				<button class="btn filter-btn" onclick="filterByShadows('Decarabia')"> Decarabia</button>
				<button class="btn filter-btn" onclick="filterByShadows('Dionysus')"> Dionysus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Dominion')"> Dominion</button>
				<button class="btn filter-btn" onclick="filterByShadows('Dyonisus')"> Dyonisus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Eligor')"> Eligor</button>
				<button class="btn filter-btn" onclick="filterByShadows('Fafnir')"> Fafnir</button>
				<button class="btn filter-btn" onclick="filterByShadows('Forneus')"> Forneus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Fuu-ki')"> Fuu-ki</button>
				<button class="btn filter-btn" onclick="filterByShadows('Ganesha')"> Ganesha</button>
				<button class="btn filter-btn" onclick="filterByShadows('Garuda')"> Garuda</button>
				<button class="btn filter-btn" onclick="filterByShadows('Girimehkala')"> Girimehkala</button>
				<button class="btn filter-btn" onclick="filterByShadows('Hanuman')"> Hanuman</button>
				<button class="btn filter-btn" onclick="filterByShadows('Hastur')"> Hastur</button>
				<button class="btn filter-btn" onclick="filterByShadows('High_Pixie')"> High Pixie</button>
				<button class="btn filter-btn" onclick="filterByShadows('Hua_Po')"> Hua Po</button>
				<button class="btn filter-btn" onclick="filterByShadows('Incubus')"> Incubus</button>
				<button class="btn filter-btn" onclick="filterByShadows('Inugami')"> Inugami</button>
				<button class="btn filter-btn" onclick="filterByShadows('Ippon-Datara')"> Ippon-Datara</button>
				<button class="btn filter-btn" onclick="filterByShadows('Isis')"> Isis</button>
				<button class="btn filter-btn" onclick="filterByShadows('Jack_Frost')"> Jack Frost</button>
				<button class="btn filter-btn" onclick="filterByShadows('Jack-o-Lantern')"> Jack-o-Lantern</button>
				<button class="btn filter-btn" onclick="filterByShadows('Jatayu')"> Jatayu</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kaiwan')"> Kaiwan</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kali')"> Kali</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kelpie')"> Kelpie</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kikuri-Hime')"> Kikuri-Hime</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kin-ki')"> Kin-ki</button>
				<button class="btn filter-btn" onclick="filterByShadows('King_Frost')"> King Frost</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kodama')"> Kodama</button>
				<button class="btn filter-btn" onclick="filterByShadows('Koppa_Tengu')"> Koppa Tengu</button>
				<button class="btn filter-btn" onclick="filterByShadows('Koropokguru')"> Koropokguru</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kumbhanda')"> Kumbhanda</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kurama_Tengu')"> Kurama Tengu</button>
				<button class="btn filter-btn" onclick="filterByShadows('Kushinada')"> Kushinada</button>
				<button class="btn filter-btn" onclick="filterByShadows('Lamia')"> Lamia</button>
				<button class="btn filter-btn" onclick="filterByShadows('Leanan_Sidhe')"> Leanan Sidhe</button>
				<button class="btn filter-btn" onclick="filterByShadows('Legion')"> Legion</button>
				<button class="btn filter-btn" onclick="filterByShadows('Lilim')"> Lilim</button>
				<button class="btn filter-btn" onclick="filterByShadows('Lilith')"> Lilith</button>
				<button class="btn filter-btn" onclick="filterByShadows('Loa')"> Loa</button>
				<button class="btn filter-btn" onclick="filterByShadows('Macabre')"> Macabre</button>
				<button class="btn filter-btn" onclick="filterByShadows('Makami')"> Makami</button>
				<button class="btn filter-btn" onclick="filterByShadows('Mandrake')"> Mandrake</button>
				<button class="btn filter-btn" onclick="filterByShadows('Mara')"> Mara</button>
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
				<button class="btn filter-btn" onclick="filterByShadows('Shiisaa')"> Shiisaa</button>
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
				<button class="btn filter-btn" onclick="filterByShadows('Throne')"> Throne</button>
				<button class="btn filter-btn" onclick="filterByShadows('Thunderbird')"> Thunderbird</button>
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

function toggleRoyalCompact(loading) {
	var compactSwitch = document.getElementById("royalCompact");
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

// Add active class to the current button (highlight it)
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
<table class="table-responsive-sm filterDiv Fuu-ki Bicorn Hanuman Anubis">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Isis Queen_Mab Sarasvati">
	<tr>
		<th colspan="5">After all, isn't it not pitiable when one denies one's own feelings?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Jatayu Kali Rangda Skadi">
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
		<td>You've got a point.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD/BAD?</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>So what?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's not my style.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kurama_Tengu Barong Nebiros Oberon">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Making excuses?</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I wasn't trying either.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Obariyon Agathion Onmoraki Cait_Sith">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Such a rude little boy...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Dating's not important.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Oberon Dionysus">
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
<table class="table-responsive-sm filterDiv Bicorn Atavaka Fuu-ki Ippon-Datara Forneus Chernobog Mara Fafnir">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I thought this up myself.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Want to join in?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kodama Obariyon Sudama">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm actually pretty busy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I never thought about it.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Onmoraki Kodama">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It pays the bills.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Andras Narcissus Barong Oberon Nebiros Baal Mithras">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Nobody, really.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It doesn't matter.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Pixie Lilim Hua_Po">
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
		<td>Impressions.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Making funny faces.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Sarasvati Titania Queen_Mab">
	<tr>
		<th colspan="5">But is it fair to my kind if only I find such happiness, leaving them all behind?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I think so.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>They can all come.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Your kind?</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Dakini Kali Skadi Alilat">
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
		<td>Nope.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I just love the elderly.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I just want you to die happy.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv King_Frost">
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
<table class="table-responsive-sm filterDiv Leanan_Sidhe High_Pixie Titania Silky Isis Queen_Mab">
	<tr>
		<th colspan="5">But this way of life in this world is all I've ever known.</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>There are other ways to live.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You had a good run.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Koppa_Tengu Kurama_Tengu Anzu Dionysus Cu_Chulainn Andras Mokoi Mithras Oberon">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Green.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't bleed or cry.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Archangel Power Throne">
	<tr>
		<th colspan="5">Can you sacrifice yourself in order to demonstrate your veneration of our Father?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I can certainly try.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No can do.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What's veneration?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv High_Pixie Apsaras Valkyrie Isis Silky Leanan_Sidhe">
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
		<td>That would take a while.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>There's no need to explain.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Just shut up...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Rakshasa Take-Minakata Choronzon Girimehkala Kumbhanda Orobas Kaiwan">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Shut up...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm secretly a kid.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Lamia Yaksini Nekomata">
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
		<td>I'm surprised you knew.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No, it's not.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's a myth.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Oni Eligor Anubis Atavaka Oni Abaddon Belphegor Bicorn">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm not known for being polite.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Koppa_Tengu Oberon Naga Mithras">
	<tr>
		<th colspan="5">Did I just see your hand shaking? Isn't your guilt tormenting you?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's just a chill.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Yeah, I can't take it...</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Black_Ooze Kumbhanda Macabre Orobas Rakshasa Girimehkala">
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
		<td>Yup...</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Not sure yet.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nah, you totally won.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Onmoraki Sudama">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Being a kid is tough.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't remember.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia Kushinada">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Mystery meat.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What are you saying?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kikuri-Hime">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Archangel Melchizedek Dominion Power">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Please tell me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I've done nothing wrong.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Archangel Power Dominion Throne">
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
		<td class='result unconfirmed'><div class='text'>GOOD / OK?</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Throne">
	<tr>
		<th colspan="5">Do you...think of me as a charlatan?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I don't think that.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I think of you as a foe.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're not one?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Obariyon Kodama Onmoraki">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Narcissus Mithras Oberon Kurama_Tengu">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>...Nope</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Fuu-ki Hanuman Anubis Forneus Abaddon Chernobog Oni">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I prefer being an adult.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I wish I was still a baby.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Queen_Mab Apsaras Parvati Valkyrie Norn Kurama_Tengu">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't worry about it.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kali Rangda">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't think so.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That just proves you're old.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Melchizedek">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kodama Obariyon">
	<tr>
		<th colspan="5">Guess what I want you to read me before you tuck me into bed!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>An animal book</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>A story about a Yakuza</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I have no idea</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Andras Dionysus Mokoi Kurama_Tengu Mithras Narcissus">
	<tr>
		<th colspan="5">Had I known things would turn out like this, I'd wish I had found the courage to ask that girl out...</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>You never had a chance.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll make sure she's happy.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv King_Frost">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That's not it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Just tell me what you know.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Power Melchizedek">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'll be the judge of that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Rakshasa Sui-ki Decarabia Take-Minakata Girimehkala Orobas Black_Ooze Ganesha">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're trying way too hard.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm not interested.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kikuri-Hime">
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
		<td>What're we getting?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Yeah.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Now's not the time.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Hua_Po Angel Lilim Kikuri-Hime">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't want a kiss.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Have some self-respect.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kikuri-Hime">
	<tr>
		<th colspan="5">Hey, if I don't die here, what do you think I'll be like in the future?</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I can't measure that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Living in darkness.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Oni Berith Koropokguru Fuu-ki Bicorn">
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
		<td>Are you okay?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I have some antacids.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That won't change anything.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kikuri-Hime">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Sudama">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Sudama Obariyon Kodama Onmoraki">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No way.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Bicorn Oni Fafnir Hanuman Baphomet">
	<tr>
		<th colspan="5">Hey. So whaddya feel when you think about the future?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Live fast, die young.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Nothing.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Ippon-Datara">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I smell sweaty.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv Lamia">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td>Where would you like to go?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Anubis Hanuman Bicorn Moloch Ippon-Datara Belphegor">
	<tr>
		<th colspan="5">Hey. Why aren't ya at school?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's after school.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't feel like going.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I actually finished school.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lilim Hua_Po">
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
		<td>Not really...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Who cares about idols?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia Nekomata">
	<tr>
		<th colspan="5">How about we live together? What kind of place do you want to live in?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I can't live with you.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Next to a convenience store.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="table-responsive-sm filterDiv Black_Ooze Rakshasa Girimehkala Mot">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I want to aim higher.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Fighting is pointless.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Anubis Forneus Bicorn Moloch Chernobog">
	<tr>
		<th colspan="5">How 'bout you, sonny? What kinda trip do you wanna take?</th>
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Don't want to go anywhere.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>A trip to hell.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Take-Minakata Sandman Orobas Black_Ooze Rakshasa Kaiwan">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>That's impossible.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Jack_Frost King_Frost">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv King_Frost">
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
		<td>You're right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>No, I do.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's all about heart.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Jack_Frost">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Jack_Frost Jack-o-Lantern King_Frost">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I want a photo.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Give me your credit card.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Oni Berith Ippon-Datara Bicorn Hanuman">
	<tr>
		<th colspan="5">Humans talk over drinks, right? How 'bout it? Hell, let me buy ya a round, sonny.</th>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>You're really paying?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm a minor.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Isis Norn Sarasvati Parvati Queen_Mab">
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
		<td>I do now.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>That doesn't matter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm always alone.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv High_Pixie Apsaras Sarasvati Isis Scathach Queen_Mab Norn Titania">
	<tr>
		<th colspan="5">I am inclined to turn you down, but if you still wish to speak, I will perhaps consider it.</th>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Do you have time?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Don't turn me down.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv King_Frost Jack_Frost">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Take-Minakata Ose Choronzon Mot Loa Rakshasa Ganesha">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>That's not happening.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Are you giving up?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Oberon Naga Narcissus Andras">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Too late.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Then let's hold hands.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Archangel Power Dominion Naga">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're tough.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't push yourself.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Oni Koropokguru Shiki-Ouji Anubis Hanuman Baphomet Moloch Bicorn">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I just have a knack for it.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>At a gym from hell.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kali Skadi Alilat Rangda">
	<tr>
		<th colspan="5">I guess women are really more social these days, finding so many fun things to do outside the home.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's so true.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Men are social too.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Is that so?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv High_Pixie Leanan_Sidhe Sarasvati Silky Yaksini Isis Queen_Mab Valkyrie Apsaras">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I apologize.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You've got the wrong idea.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Rakshasa Orobas Kaiwan Ose Mot Macabre">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Not at all.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Why does that matter?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Nekomata Yaksini Lamia Lilith">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Grovel before me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I don't know.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Narcissus Koppa_Tengu Dionysus">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>...I could get used to it.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It pains my heart...</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Isis Leanan_Sidhe Valkyrie Sarasvati">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Go impulse shopping.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Don't be so selfish.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Rangda Skadi">
	<tr>
		<th colspan="5">I suppose it makes no difference if you kill me or if I die just a little bit later, dearie.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's right</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That isn't true</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's still a long ways off</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kali Rangda Dakini">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It can't be helped.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's for your own good.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Titania Norn Parvati Queen_Mab Valkyrie">
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
		<td>You're right.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It keeps me busy.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's better than here.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Dakini Kali">
	<tr>
		<th colspan="5">I think dying alone isn't so bad, dearie, but isn't living alone in the first place the real tragedy?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="table-responsive-sm filterDiv Onmoraki Kodama">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia Ame-no-Uzume Nekomata Yaksini">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>What are you getting at?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You have a boyfriend?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kali Rangda Alilat Dakini">
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
		<td>I'll introduce you to them later.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Rangda Skadi Dakini Kali Alilat">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia">
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
<table class="table-responsive-sm filterDiv Kushinada">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia Kushinada">
	<tr>
		<th colspan="5">I wonder if it's about time I quit this job.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Hang in there.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>That's a good idea.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>And then what?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Parvati Sarasvati Isis Queen_Mab Scathach Norn Titania">
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
		<td>It could be.</td>
		<td class='result unconfirmed'><div class='text'>GOOD / OK</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No way.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's fate.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Koppa_Tengu Andras Kurama_Tengu Oberon Naga Barong">
	<tr>
		<th colspan="5">I would have never accepted this task if I knew it would involve this sort of suffering.</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Uninformed choices are bad.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Complaining won't help.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Andras Narcissus Kurama_Tengu Oberon Nebiros Naga">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>A deal with the enemy?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can't trust you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Yaksini Lamia Ame-no-Uzume Nekomata Lilith Kushinada">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>You're not making sense.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>What would you like?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lilim">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Then who's the real enemy?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Bicorn Berith Shiki-Ouji Hanuman Shiisaa Koropokguru Anubis Baphomet Moloch Thor">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'll have some more fun first.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I won't make you suffer.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Fuu-ki Bicorn Koropokguru Belphegor Chernobog Atavaka Oni">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You dirty old man.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Orthrus Nue Shiisaa Anzu">
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
<table class="table-responsive-sm filterDiv Yaksini Nekomata Ame-no-Uzume">
	<tr>
		<th colspan="5">If your girlfriend asked if you wanted to have dinner with "everybody", what you you say?</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm busy.</td>
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
<table class="table-responsive-sm filterDiv Lamia Nekomata">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Naga Barong Andras">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Mandrake Angel Pixie Hua_Po">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No strings attached?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I've got enough on my plate...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Jack-o-Lantern Jack_Frost King_Frost">
	<tr>
		<th colspan="5">I'm a super popular Shadow, you hee-know. My fans won't just sit around and take this, ho.</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Jack_Frost King_Frost Jack-o-Lantern">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Maybe.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Cougars are all the rage now.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>How much do you want?</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Dionysus Oberon Cu_Chulainn Narcissus Kurama_Tengu">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Not necessarily.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Anyone will do.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Loa Kaiwan">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm waiting.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kikuri-Hime Angel">
	<tr>
		<th colspan="5">I'm sure there're other people in the world who'd irritate you more. C'mon, tell me.</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No one bothers me.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Skadi Rangda Dakini Alilat">
	<tr>
		<th colspan="5">I'm thinking that maybe I should act more grandmotherly. How can I go ahead and do that for you?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Scold me every so often.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You don't have to do anything.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Barong">
	<tr>
		<th colspan="5">I'm well-connected, okay? I know some people that are pretty complicated.</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Complicated...?</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="table-responsive-sm filterDiv Atavaka">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv Lilim">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Cait_Sith Onmoraki Sudama Obariyon">
	<tr>
		<th colspan="5">Is it 'cause I wasn't a "good kid"?</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It has nothing to do with this.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Sui-ki Girimehkala Decarabia Kaiwan Ose Ganesha">
	<tr>
		<th colspan="5">Is it just me, or does something stink?</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's coming from you.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I smell a lie.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Melchizedek">
	<tr>
		<th colspan="5">Is it not a breeding ground for impudent humans? How do you view this world of yours?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Full of corrupt adults.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Plenty of places to shop.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Looks normal to me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Leanan_Sidhe Isis Silky Valkyrie High_Pixie Parvati Norn Apsaras">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK/GOOD?</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD / OK</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Obariyon Onmoraki Kodama">
	<tr>
		<th colspan="5">Is it okay if I get mad right now?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Do it.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Please don't.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're so cute.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kikuri-Hime Lilim">
	<tr>
		<th colspan="5">Is it only for men? Where did you get it?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Internet shopping.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's not available for sale.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Lamia">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv Isis Norn Queen_Mab">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I can't promise that.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's a matter of feeling.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Dakini Rangda Alilat Skadi">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I love someone else.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
		<td>Yea.</td>
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
		<td>It's for your own good.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Onmoraki">
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
<table class="table-responsive-sm filterDiv Archangel Power">
	<tr>
		<th colspan="5">It is to become aware of the gaze of our Father, who watches over you with loving grace.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>I don't understand.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I feel his gaze.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I prefer a harsher stare.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kin-ki">
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
<table class="table-responsive-sm filterDiv Archangel Leanan_Sidhe">
	<tr>
		<th colspan="5">It seems the Son of Man have denounced the word of our father. Tell me, what worth have you found?</th>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I can survive alone.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Find it for me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Legion Mot Choronzon Ganesha Ose">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I had no idea.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This'll be your deathday too.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Mithras Kurama_Tengu Mokoi Koppa_Tengu Nebiros Andras Narcissus">
	<tr>
		<th colspan="5">It's cliched, but we could talk about life... Ask each other things like what sort of girls we're into...</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No preference.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="table-responsive-sm filterDiv Mokoi Koppa_Tengu Oberon Naga Dionysus Baal Mithras Nebiros">
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
		<td>I need your help.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Lick my boots.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Are you sure it's fine?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kikuri-Hime">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lilim Hua_Po Kikuri-Hime">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You should love your parents.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Why not come to my place?</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Take-Minakata Incubus Girimehkala Orthrus Rakshasa Sandman Kaiwan">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's part of my face.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>My apologies.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Leanan_Sidhe High_Pixie Apsaras Isis Parvati Queen_Mab Valkyrie Sarasvati">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I didn't feel an "aura".</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>But we may never meet again.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia Lilith">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Definitely not.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Rakshasa Take-Minakata Black_Ooze Orobas Decarabia Girimehkala Kumbhanda">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Hanuman Bicorn Koropokguru Oni Baphomet Thor">
	<tr>
		<th colspan="5">Know how they say, "Be kind ta yer elders"? Has no one ever taught ya that?</th>
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't care.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I don't want to grow old.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Archangel Power Melchizedek">
	<tr>
		<th colspan="5">Let me hear you utter words of repentance.</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>"Words of repentance."</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Not sorry.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Kelpie Fafnir Koropokguru">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Don't expect it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Hua_Po Mandrake Lilim Angel Kikuri-Hime">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Forgive me.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It was self-defense.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Orthrus Nue Cerberus Kelpie Makami Yamata-no-Orochi Chimera Hastur Slime">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't want to eat you.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'll mince you.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Slime Unicorn Garuda">
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
		<td>Academics.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Empathy.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Girl power.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Makami Orthrus Shiisaa Thoth Jatayu">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Anzu Orthrus Inugami Nue Makami Shiisaa Thoth Arahabaki Unicorn">
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
		<td>Youthfulness.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Cuteness.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Luckiness.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Nue Hastur Jatayu Yamata-no-Orochi Byakhee Slime Chimera">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Same goes for me</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Want to order something?</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Orthrus Jatayu Garuda">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't have any.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Hunger is the best ingredient.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Byakhee Arahabaki Jatayu">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Why show mercy to my enemy?</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>...I got nothing.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Kikuri-Hime Angel Hua_Po Lilim">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>How is your luck in romance?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Archangel Power">
	<tr>
		<th colspan="5">Name a calamity that you can bear.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Make it crowded where I shop.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Give me violence.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No calamities, please.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Apsaras Sarasvati High_Pixie Valkyrie Isis">
	<tr>
		<th colspan="5">No matter the crime, humans treat it more lightly if the perpetrator is a minor, do they not? Ah, so I suppose you commit such extreme acts because you know you won't be punished harshly…</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Age doesn't matter.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>This isn't extreme.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Skadi Rangda">
	<tr>
		<th colspan="5">Now, people don't even know who lives next door to them. Shouldn't we know our neighbors better?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's saddening.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't really think about it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Privacy is important.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kali Rangda Skadi Alilat">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Pixie Mandrake Angel Succubus Hua_Po Lilim">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Just get plastic surgery.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'll take responsibility.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Throne Power">
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
		<td>If it's what you want.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>What are you telling me?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm a minor.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kaiwan Mot Girimehkala Sui-ki Sandman Ganesha">
	<tr>
		<th colspan="5">Seriously, cosplaying in a place like this? Are you just bored outta your mind?</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm actually very busy.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Shut up!</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Obariyon">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's your fault for being tricked.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Kodama">
	<tr>
		<th colspan="5">She said, "I'll buy it for you on the way home," but she didn't buy it for me! That's SO unfair, right?!</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>That's not unfair.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's your fault for being tricked.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I'll buy it for you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Lamia">
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
<table class="table-responsive-sm filterDiv Thoth Cerberus Byakhee Arahabaki Slime">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I could carry that weight.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't get it...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Girimehkala Kaiwan Choronzon Kumbhanda Legion Sandman">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>No... Nothing at all...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Dance for me!</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia Nekomata Yaksini">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Thoth Kelpie Shiisaa Inugami Unicorn Chimera Byakhee Makami Orthrus Slime">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>This is a difficult topic...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It is fun, actually.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
<table class="table-responsive-sm filterDiv Dakini Skadi">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>They must be young inside.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Shiki-Ouji Koropokguru Berith Fuu-ki Bicorn Oni Belphegor Forneus Chernobog Fafnir">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I got bad luck.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Rangda">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Never heard of that.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv King_Frost">
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
		<td>Sorry.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td>You go home.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Apsaras Valkyrie High_Pixie Isis Norn">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Archangel">
	<tr>
		<th colspan="5">That is to say, we are brothers.  There is no reason for us to fight.</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Leave my parents out of this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You may be right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>But you're a Shadow.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Power Throne">
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
		<td>I never considered it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>This power is all mine.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't know.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Pisaca Choronzon Ganesha">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Now way.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm going feral!</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Koppa_Tengu Mithras Mokoi Andras Oberon">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Actually... I'm bad.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv Yaksini Lamia Lilith Nekomata">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Makami Arahabaki Inugami Kelpie Nue Makami Orthrus Nekomata Yamata-no-Orochi Hastur Cerberus">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Not really.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Let me touch your paw.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Sui-ki Sandman Kumbhanda Take-Minakata Legion Choronzon Rakshasa Black_Ooze Ganesha">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kali Rangda">
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
		<td>It's what's in.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Archangel Dominion">
	<tr>
		<th colspan="5">Think carefully. I am not the one you should detest.</th>
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
		<td>[...]</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Throne Power Archangel">
	<tr>
		<th colspan="5">Think carefully. I cannot be destroyed. Desist from this pointlessness.</th>
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
		<td>Then I shall desist.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv King_Frost Jack-o-Lantern Jack_Frost">
	<tr>
		<th colspan="5">This is all some kind of TV thing, hee-ho! Where's the camera?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What's all this now?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>This is real.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Obariyon Cait_Sith Agathion Onmoraki">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What? No, you're wrong...</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Um, are things okay at home?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Jack-o-Lantern Jack_Frost">
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
		<td>I can't image it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Throne Archangel Power Dominion">
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
		<td>Leave the future to me.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I need your guidance.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't get it.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Yaksini Lamia Nekomata Ame-no-Uzume Kushinada">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Should I go instead?</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Girls...?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Girimehkala">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's coming from you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Power Archangel Throne">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No complaints here.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I can't get a girlfriend.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Archangel Melchizedek Dominion Power">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No need to be so dramatic.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I decline.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kushinada">
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
		<td>Go home then.</td>
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
		<td>Let's go home together.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Lilim Kikuri-Hime Angel">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Rangda Kali Dakini">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I didn't know that.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Who cares?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kodama Obariyon Sudama">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Let's play a video game.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Cruise for chicks.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kurama_Tengu Nebiros Baal">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Don't play the victim.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing in particular.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Jatayu">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Slaughter.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Bicorn Thor Mara Fuu-ki Eligor">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>All sorts of things.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Protein.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Yaksini Lamia">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not interested.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What are you talking about?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Mithras Koppa_Tengu Oberon Naga Nebiros">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Nothing, really.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>A killing spree.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Koppa_Tengu Oberon Naga Dionysus">
	<tr>
		<th colspan="5">What if I was a human? Then, what you're doing... well, it'd be a criminal act!</th>
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>That can't be true.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
<table class="table-responsive-sm filterDiv Ippon-Datara Oni Shiki-Ouji Bicorn Koropokguru Moloch">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Why do we fight?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't really know...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Titania Isis Queen_Mab Valkyrie">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Egotistical women.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm not irritated.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Eligor Bicorn Hanuman Anubis">
	<tr>
		<th colspan="5">What kinda "fate" do ya think there is in this meetin' between me and you?</th>
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I want to end this fate.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Bicorn Atavaka Forneus Hanuman">
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
		<td>You won't suffer long.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>A coupon for a massage by me.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'll be at your side until the end.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Loa Macabre Incubus Choronzon Ganesha Ose">
	<tr>
		<th colspan="5">What kinda guys piss you off?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>Pissy guys.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Guys with no sense of humor. </td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I never get mad. </td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Pixie">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Sudama Cait_Sith Onmoraki Kodama Agathion">
	<tr>
		<th colspan="5">What was that, anyway?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>A coupon.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Nebiros Cu_Chulainn Barong Dyonisus">
	<tr>
		<th colspan="5">What was... the cause of my defeat?</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Just bad luck.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm not telling.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Unicorn Inugami Nue Cerberus Makami Jatayu">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Macabre Choronzon Loa Ose">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll forget it happened.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Take-Minakata Girimehkala Orobas">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'll play nice.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv Obariyon Kodama Onmoraki">
	<tr>
		<th colspan="5">What's it like to be all kissy face with somebody?</th>
	</tr>
	<tr>
		<td></td>
		<td class='subheader'>gl<span class='extra'>oomy</span></td>
		<td class='subheader'>ir<span class='extra'>ritable</span></td>
		<td class='subheader'>ti<span class='extra'>mid</span></td>
		<td class='subheader'>up<span class='extra'>beat</span></td>
	</tr>
	<tr>
		<td>It's incredible...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I shouldn't tell you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Ask your parents.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Bicorn Thor Berith Shiki-Ouji Oni Anubis Moloch">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're ugly.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Nothing's wrong.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Skadi Dakini Rangda Alilat">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm just that good.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You've grown old.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Pixie Hua_Po Mandrake Succubus Angel">
	<tr>
		<th colspan="5">When it came right down to it, you couldn't do anything to me!</th>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>How could you tell?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What do you want me to do?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kodama Obariyon">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Worcestershire sauce.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't add anything.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Obariyon Onmoraki">
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
		<td>I had no dream.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>A winner in society.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Sudama Obariyon Kodama">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Koppa_Tengu Naga Mithras Andras Barong Oberon">
	<tr>
		<th colspan="5">Who the blazes do you think you are?</th>
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm ME!</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I don't owe you an answer.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Rangda Dakini Skadi Kali Alilat">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm here for the loot.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Just 'cause.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Sarasvati Isis High_Pixie">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Nue Shiisaa Inugami Orthrus Thoth Thunderbird Unicorn Jatayu Byakhee Cerberus">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>For girls.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I just felt like it.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Slime Anzu Thunderbird Jatayu Garuda Yamata-no-Orochi Arahabaki Cerberus">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Because I see an enemy.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I don't actually know.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Nue Orthrus Anzu Arahabaki Kelpie Shiisaa Inugami Makami Mothman Byakhee Hastur Thoth Jatayu">
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Should I take off my shoes?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Anzu Nue Chimera Thunderbird Arahabaki Jatayu">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I want to cherish you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>You're not a beast.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Nue Yamata-no-Orochi Garuda">
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
<table class="table-responsive-sm filterDiv Rakshasa Take-Minakata Ose Incubus Black_Ooze Orobas Sandman Decarabia">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>There's something I must do.</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I want girls to like me.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Isis High_Pixie Valkyrie Norn Scathach">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I can't just leave you.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Is that reverse psychology?</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Skadi Kali Rangda">
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
		<td>I suppose so.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Sounds like a drag.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No one invites me to reunions.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Apsaras Norn Sarasvati Valkyrie Titania">
	<tr>
		<th colspan="5">Would you do to anyone else what you're doing to me now?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No, I wouldn't.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>This is a special exception.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
<table class="table-responsive-sm filterDiv Forneus Moloch Hanuman Mara Fafnir Fuu-ki">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's all the same.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Ippon-Datara Bicorn Hanuman Moloch">
	<tr>
		<th colspan="5">...Y'know what I'm gettin' at, right? Ya think ya could let me go see my girl?</th>
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
		<td>I'll consider it.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>What kind of girl is she?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Nue Slime Cerberus Hastur">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're just a sore loser.</td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv Mandrake Succubus Angel Pixie">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It won't?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>It's for self-improvement.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Andras Oberon Naga">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Well, I got a little lost.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't remember.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Anzu Cu_Chulainn Kurama_Tengu Mithras">
	<tr>
		<th colspan="5">You do realize it's useless to go waving that thing around aimlessly.</th>
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Don't act so tough.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Not as useless as you.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Leanan_Sidhe Silky Isis Valkyrie Titania Apsaras">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I understand.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>What do you mean?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Slime Thunderbird Inugami Anzu Jatayu Arahabaki">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Thunderbird Cerberus Arahabaki Garuda Nue Mothman Slime Jatayu">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not sleepy.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>After I'm done with this.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Nue Orthrus Inugami Makami Thoth Mothman Thunderbird">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>My ex-girlfriend...</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Quiet, I'm killing you now.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Archangel Throne">
	<tr>
		<th colspan="5">You have appeared to test my adoration of our Father. Yes, you are... the Tempter</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>You're mistaken.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>Are you okay?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Orthrus Unicorn Shiisaa Inugami Makami Nue Thunderbird">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>A grand funeral.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I won't die.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Leanan_Sidhe High_Pixie Valkyrie Sarasvati Isis">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>That's right.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I have ulterior motives.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Sandman Kaiwan Choronzon Girimehkala Decarabia Legion Ose Ganesha">
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
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>Like I care.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>You should "watch" your mouth.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv King_Frost">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
<table class="table-responsive-sm filterDiv Lamia Yaksini Nekomata Lilith Ame-no-Uzume">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lamia Ame-no-Uzume Nekomata Kushinada Yaksini">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>No, thanks.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>I already get enough, actually.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Rangda Skadi Dakini Kali">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>They're not great...</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>At least I'm popular.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv King_Frost">
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
		<td>Yeah! Nice you meetcha!</td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm a transfer student.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>No.</td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Chimera Arahabaki Anzu Thoth Cerberus Thunderbird">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I don't mind.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's for love.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Rangda Skadi Dakini Alilat">
	<tr>
		<th colspan="5">You were so sure of yourself, so it's embarrassing now to admit you're struggling here. Right?</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Power Archangel Dominion">
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
		<td>Omnipotent?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm not beleaguered.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>There's someone I want to save.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Valkyrie Apsaras Titania Queen_Mab Sarasvati Norn">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>I'm prepared for the worst.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>How much do you want?</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Kumbhanda Decarabia Sui-ki">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Skadi Kali Rangda Dakini Alilat">
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
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Don't worry about it.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>It's worth it.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
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
<table class="table-responsive-sm filterDiv Onmoraki">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm not mature anyway.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Lilim Kikuri-Hime">
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
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>What's the right way, then?</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
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
<table class="table-responsive-sm filterDiv Lilim Pixie Kikuri-Hime Hua_Po">
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
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I choose my targets carefully.</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
	<tr>
		<td>I'm serious about this.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv None">
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
		<td class='result unconfirmed'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Onmoraki Sudama Cait_Sith Agathion">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>I'm good at PE.</td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
	<tr>
		<td>Shut up.</td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Black_Ooze Sandman Girimehkala Rakshasa Kumbhanda Orobas Kaiwan Legion">
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
	</tr>
	<tr>
		<td>It's for self-defense.</td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
	<tr>
		<td>Pretty cool, huh?</td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>OK</div><div class='symbol'>💦</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
	</tr>
</table>
<table class="table-responsive-sm filterDiv Jack_Frost King_Frost">
	<tr>
		<th colspan="5"> ...You've come from some other company to scout me-hee out. There's no mistaking it, ho!</th>
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
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
		<td class='result'><div class='text'>GOOD</div><div class='symbol'>🎶</div></td>
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
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result'><div class='text'>-</div><div class='symbol'></div></td>
		<td class='result unconfirmed'><div class='text'>BAD</div><div class='symbol'>💢</div></td>
	</tr>
</table>
</div>

<!-- LOCAL STORAGE OF SWITCH STATE -->
<script>
window.onload = onPageLoad();

function onPageLoad() {
	var switchState = JSON.parse(localStorage["royalCompact"] || false);
	var compactSwitch = document.getElementById("royalCompact");
	if (switchState) {
		compactSwitch.checked = true;
		toggleRoyalCompact(true);
	}
}
</script>