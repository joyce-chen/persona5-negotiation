<div class="input-group">
	<input class="form-control py-2 border-right-0 border" type="text" id="searchBar" onkeyup="filterShadows()" placeholder="Search for shadows by name, description, personality etc.." title="Type in a shadow">
	<span class="input-group-append">
		<div class="input-group-text bg-transparent"><i class="fa fa-search"></i></div>
	</span>
</div>

<script>
function filterShadows() {
   var input, filter, headers, tables, tableRowCount, tr;
   input = document.getElementById("searchBar");
   filter = input.value.toUpperCase();
   headers = document.getElementsByTagName("h5");
   tables = document.getElementsByTagName("table");
   tableRowCount = [];

   for (i = 0; i < tables.length; i++) {
      tableRowCount.push(tables[i].rows.length);
   }
   
   for (i = 0; i < tables.length; i++) {
      tr = tables[i].getElementsByTagName("tr");
      var hiddenCount = 0;

      for (j = 0; j < tr.length; j++) {
         td = tr[j].getElementsByTagName("td")[0];
         if (td) {
            var levelCol = tr[j].getElementsByTagName("td")[0].textContent.toUpperCase();
            var nameCol = tr[j].getElementsByTagName("td")[1].textContent.toUpperCase();
            var desCol = tr[j].getElementsByTagName("td")[2].textContent.toUpperCase();
            var arcCol = tr[j].getElementsByTagName("td")[3].textContent.toUpperCase();
            var perCol = tr[j].getElementsByTagName("td")[4].textContent.toUpperCase();
            if (nameCol.indexOf(filter) > -1 || desCol.indexOf(filter) > -1 || arcCol.indexOf(filter) > -1 || perCol.indexOf(filter) > -1) {
               tr[j].style.display = "";
            } else {
               tr[j].style.display = "none";
               hiddenCount = hiddenCount + 1;
            }
         }
      }

      if (hiddenCount == tableRowCount[i] - 1) {
         tables[i].style.display = "none";
         headers[i].style.display = "none";
      } else {
         tables[i].style.display = "";
         headers[i].style.display = "";
      }
   }
}
</script>

<br>

##### 1 - Kamoshida's Palace - Castle

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>2</td>
      <td>Jack-o'-Lantern</td>
      <td>Crypt-dwelling Pyromaniac</td>
      <td>Magician</td>
      <td>Gloomy</td>
      <td>Ice, Wind</td>
   </tr>
   <tr>
      <td>2</td>
      <td>Pixie</td>
      <td>Beguiling Girl</td>
      <td>Lovers</td>
      <td>Timid</td>
      <td>Gun, Ice, Curse</td>
   </tr>
   <tr>
      <td>3</td>
      <td>Agathion</td>
      <td>Apprentice in a Jug</td>
      <td>Chariot</td>
      <td>Timid</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>3</td>
      <td>Mandrake</td>
      <td>Gallows-Flower</td>
      <td>Death</td>
      <td>Upbeat</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>4</td>
      <td>Bicorn</td>
      <td>Dirty Two-horned Beast</td>
      <td>Hermit</td>
      <td>Gloomy</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>5</td>
      <td>Cait Sith <span class="badge badge-danger">Royal</span></td>
      <td>Hunting Puss in Boots</td>
      <td>Magician</td>
      <td>Upbeat</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>5</td>
      <td>Incubus</td>
      <td>Bedside Brute</td>
      <td>Devil</td>
      <td>Timid</td>
      <td>Fire, Bless</td>
   </tr>
   <tr>
      <td>6</td>
      <td>Kelpie</td>
      <td>Mad Marsh Horse</td>
      <td>Strength</td>
      <td>Upbeat</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>6</td>
      <td>Silky</td>
      <td>Troublesome Housemaid</td>
      <td>Priestess</td>
      <td>Gloomy</td>
      <td>Fire, Elec</td>
   </tr>
   <tr>
      <td>7</td>
      <td>Succubus</td>
      <td>Twilight Prostitute</td>
      <td>Moon</td>
      <td>Gloomy</td>
      <td>Wind, Bless</td>
   </tr>
   <tr>
      <td>9</td>
      <td>Angel</td>
      <td>Zealous Messenger</td>
      <td>Justice</td>
      <td>Upbeat</td>
      <td>Gun, Curse</td>
   </tr>
   <tr>
      <td>9</td>
      <td>Berith</td>
      <td>Brutal Cavalryman</td>
      <td>Hierophant</td>
      <td>Irritable</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>14</td>
      <td>Archangel</td>
      <td>Heavenly Punisher</td>
      <td>Justice</td>
      <td>Irritable</td>
      <td>Elec, Curse</td>
   </tr>
   <tr>
      <td>16</td>
      <td>Eligor</td>
      <td>War-hungry Horseman</td>
      <td>Emperor</td>
      <td>Upbeat</td>
      <td>Elec</td>
   </tr>
   <!-- <tr>
      <td>N/A</td>
      <td>Eligor</td>
      <td>Guard Captain</td>
      <td>Emperor</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Bicorn</td>
      <td>Dirty Two-horned Beast</td>
      <td>Hermit</td>
      <td>Miniboss Adds</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Belphegor</td>
      <td>Guard Captain</td>
      <td>Tower</td>
      <td>Miniboss</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Archangel</td>
      <td>Heavenly Punisher</td>
      <td>Justice</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Mara</td>
      <td>Torn King of Desire</td>
      <td>Tower</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr> -->
</table>

##### 2 - Madarame's Palace - Museum

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>9</td>
      <td>Hua Po</td>
      <td>Girl of the Hanging Tree</td>
      <td>Hanged Man</td>
      <td>Irritable</td>
      <td>Gun, Ice</td>
   </tr>
   <tr>
      <td>9</td>
      <td>Koropokguru</td>
      <td>Leafy Old Man</td>
      <td>Hermit</td>
      <td>Timid</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>9</td>
      <td>Mokoi</td>
      <td>Night-Walking Warrior</td>
      <td>Death</td>
      <td>Gloomy</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>10</td>
      <td>Regent</td>
      <td>(Treasure Demon)</td>
      <td>Emperor</td>
      <td>None</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>11</td>
      <td>Apsaras</td>
      <td>Waterside Nymph</td>
      <td>Priestess</td>
      <td>Timid</td>
      <td>Fire, Elec</td>
   </tr>
   <tr>
      <td>11</td>
      <td>Jack Frost</td>
      <td>Mocking Snowman</td>
      <td>Magician</td>
      <td>Timid</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>11</td>
      <td>Koppa Tengu</td>
      <td>Foolish Monk</td>
      <td>Temperance</td>
      <td>Upbeat</td>
      <td>Ice, Bless</td>
   </tr>
   <tr>
      <td>12</td>
      <td>Onmoraki</td>
      <td>Corpse Bird</td>
      <td>Moon</td>
      <td>Gloomy</td>
      <td>Ice, Bless</td>
   </tr>
   <tr>
      <td>13</td>
      <td>Ame-no-Uzume <span class="badge badge-danger">Royal</span></td>
      <td>Captivating Dancer</td>
      <td>Lovers</td>
      <td>Upbeat</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>14</td>
      <td>Inugami</td>
      <td>Possessing Dog Ghost</td>
      <td>Hanged Man</td>
      <td>Timid</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>15</td>
      <td>Makami</td>
      <td>Hunting Wolf Spirit</td>
      <td>Temperance</td>
      <td>Gloomy</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>15</td>
      <td>Shiisaa <span class="badge badge-danger">Royal</span></td>
      <td>Rooftop Lion</td>
      <td>Strength</td>
      <td>Upbeat</td>
      <td>Psy, Curse</td>
   </tr>
   <tr>
      <td>20</td>
      <td>Nue</td>
      <td>Night Chimera</td>
      <td>Death</td>
      <td>Irritable</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>21</td>
      <td>Shiki-Ouji</td>
      <td>Bringer of Misfortune</td>
      <td>Chariot</td>
      <td>Irritable</td>
      <td>Nuke</td>
   </tr>
   <!-- <tr>
      <td>N/A</td>
      <td>Nue</td>
      <td>Security Shadow</td>
      <td>Death</td>
      <td>Miniboss</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Ippon-Datara</td>
      <td>Embittered Blacksmith</td>
      <td>Hermit</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Koppa Tengu</td>
      <td>Foolish Monk</td>
      <td>Temperance</td>
      <td>Miniboss Adds</td>
      <td>Ice, Bless</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Kurama Tengu</td>
      <td>Monk of the Valley</td>
      <td>Hermit</td>
      <td>Miniboss</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Makami</td>
      <td>Hunting Wolf Spirit</td>
      <td>Temperance</td>
      <td>Miniboss</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Arahabaki</td>
      <td>Awakened God</td>
      <td>Hermit</td>
      <td>Miniboss</td>
      <td>Wind</td>
   </tr> -->
</table>

##### 3 - Kaneshiro's Palace - Bank

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>15</td>
      <td>Queen's Necklace</td>
      <td>(Treasure Demon)</td>
      <td>Empress</td>
      <td>None</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>16</td>
      <td>High Pixie</td>
      <td>Prankster Leader</td>
      <td>Fool</td>
      <td>Upbeat</td>
      <td>Gun, Nuke</td>
   </tr>
   <tr>
      <td>17</td>
      <td>Nekomata</td>
      <td>Ascended Feline</td>
      <td>Magician</td>
      <td>Upbeat</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>17</td>
      <td>Orobas</td>
      <td>Equine Sage</td>
      <td>Hierophant</td>
      <td>Gloomy</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>18</td>
      <td>Black Ooze</td>
      <td>Pulsing Mud</td>
      <td>Moon</td>
      <td>Timid</td>
      <td>Elec, Psy, Bless</td>
   </tr>
   <tr>
      <td>19</td>
      <td>Leanan Sidhe</td>
      <td>Jealous Lover</td>
      <td>Lovers</td>
      <td>Timid</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>20</td>
      <td>Oni</td>
      <td>Chivalrous Fiend</td>
      <td>Strength</td>
      <td>Upbeat</td>
      <td>None</td>
   </tr>
   <tr>
      <td>20</td>
      <td>Yaksini</td>
      <td>Human-eating Lady</td>
      <td>Empress</td>
      <td>Irritable</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>21</td>
      <td>Orthrus</td>
      <td>Twin-headed Guardian</td>
      <td>Hanged Man</td>
      <td>Gloomy</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>24</td>
      <td>Rakshasa</td>
      <td>Battle Fiend</td>
      <td>Strength</td>
      <td>Upbeat</td>
      <td>Wind, Bless</td>
   </tr>
   <tr>
      <td>21</td>
      <td>Sui-ki</td>
      <td>Raging Water Demon</td>
      <td>Moon</td>
      <td>Gloomy</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>26</td>
      <td>Take-Minakata</td>
      <td>Defeated Avenger</td>
      <td>Hanged Man</td>
      <td>Irritable</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>31</td>
      <td>Kurama Tengu</td>
      <td>Monk of the Valley</td>
      <td>Hermit</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <!-- <tr>
      <td>N/A</td>
      <td>Sui-ki</td>
      <td>Raging Water Demon</td>
      <td>Moon</td>
      <td>Miniboss</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Oni</td>
      <td>Chivalrous Fiend</td>
      <td>Strength</td>
      <td>Miniboss Adds</td>
      <td>None</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Orthrus</td>
      <td>Twin-headed Guardian</td>
      <td>Hanged Man</td>
      <td>Miniboss</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Orobas</td>
      <td>Equine Sage</td>
      <td>Hierophant</td>
      <td>Miniboss</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Fuu-ki</td>
      <td>Tornado Devil</td>
      <td>Star</td>
      <td>Miniboss</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Sui-ki</td>
      <td>Raging Water Demon</td>
      <td>Moon</td>
      <td>Miniboss</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Kin-ki</td>
      <td>Samurai Killer</td>
      <td>Chariot</td>
      <td>Miniboss</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Kumbhanda</td>
      <td>Life-Draining Spirit</td>
      <td>Hermit</td>
      <td>Miniboss</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Cerberus</td>
      <td>Guard Dog of Hades</td>
      <td>Chariot</td>
      <td>Miniboss</td>
      <td>Ice</td>
   </tr> -->
</table>

##### 4 - Futaba's Palace - Tomb

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>20</td>
      <td>Stone of Scone</td>
      <td>(Treasure Demon)</td>
      <td>Fortune</td>
      <td>None</td>
      <td>All</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>24</td>
      <td>Sandman</td>
      <td>Envoy of Slumber</td>
      <td>Magician</td>
      <td>Upbeat</td>
      <td>Fire, Elec</td>
   </tr>
   <tr>
      <td>24</td>
      <td>Naga</td>
      <td>Cavern Snakeman</td>
      <td>Hermit</td>
      <td>Gloomy</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>25</td>
      <td>Anzu</td>
      <td>Thief of Tablets</td>
      <td>Hierophant</td>
      <td>Timid</td>
      <td>Gun, Nuke</td>
   </tr>
   <tr>
      <td>26</td>
      <td>Isis</td>
      <td>She of Life and Death</td>
      <td>Priestess</td>
      <td>Irritable</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>26</td>
      <td>Lamia</td>
      <td>Slithering Snakewoman</td>
      <td>Empress</td>
      <td>Gloomy</td>
      <td>Ice, Nuke</td>
   </tr>
   <tr>
      <td>27</td>
      <td>Andras</td>
      <td>Menacing Owlman</td>
      <td>Devil</td>
      <td>Timid</td>
      <td>Fire, Bless</td>
   </tr>
   <tr>
      <td>34</td>
      <td>Anubis</td>
      <td>Bearer of the Scales</td>
      <td>Judgement</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <tr>
      <td>36</td>
      <td>Thoth</td>
      <td>Chanting Baboon</td>
      <td>Emperor</td>
      <td>Irritable</td>
      <td>Psy</td>
   </tr>
   <!-- <tr>
      <td>N/A</td>
      <td>Garuda</td>
      <td>Raging Bird God</td>
      <td>Star</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Mot</td>
      <td>Coffin-borne God</td>
      <td>Death</td>
      <td>Miniboss</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Naga</td>
      <td>Cavern Snakeman</td>
      <td>Hermit</td>
      <td>Miniboss Adds</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Lamia</td>
      <td>Slithering Snakewoman</td>
      <td>Empress</td>
      <td>Miniboss Adds</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Ailat</td>
      <td>Decadent False God</td>
      <td>Empress</td>
      <td>Miniboss</td>
      <td>?</td>
   </tr> -->
</table>

##### 5 - Okumura's Palace - Space Station

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>25</td>
      <td>Koh-i-Noor</td>
      <td>(Treasure Demon)</td>
      <td>Priestess</td>
      <td>None</td>
      <td>Gun</td>
   </tr>
   <tr>
      <td>32</td>
      <td>Decarabia</td>
      <td>Vicious Pentagram</td>
      <td>Councillor</td>
      <td>Timid</td>
      <td>Phys</td>
   </tr>
   <tr>
      <td>32</td>
      <td>Lilim</td>
      <td>Woman Who Brings Ruin</td>
      <td>Devil</td>
      <td>Gloomy</td>
      <td>Wind, Bless</td>
   </tr>
   <tr>
      <td>33</td>
      <td>Mothman</td>
      <td>Vampire Moth</td>
      <td>Moon</td>
      <td>Timid</td>
      <td>Gun</td>
   </tr>
   <tr>
      <td>34</td>
      <td>Thunderbird <span class="badge badge-danger">Royal</span></td>
      <td>Storm-Invoking Ptarmigan</td>
      <td>Sun</td>
      <td>Upbeat</td>
      <td>Psy, Curse</td>
   </tr>
   <tr>
      <td>35</td>
      <td>Arahabaki</td>
      <td>Awakened God</td>
      <td>Hermit</td>
      <td>Gloomy</td>
      <td>Psy, Nuke</td>
   </tr>
   <tr>
      <td>36</td>
      <td>Kaiwan</td>
      <td>Wishless Star</td>
      <td>Star</td>
      <td>Timid</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>37</td>
      <td>Belphegor</td>
      <td>Ambassador of Filth</td>
      <td>Tower</td>
      <td>Timid</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>39</td>
      <td>Mithras</td>
      <td>Dark Sun</td>
      <td>Sun</td>
      <td>Gloomy</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>42</td>
      <td>Kumbhanda</td>
      <td>Life-Draining Spirit</td>
      <td>Hermit</td>
      <td>Gloomy</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>43</td>
      <td>Girimehkala</td>
      <td>Rebellious Elephant</td>
      <td>Moon</td>
      <td>Irritable</td>
      <td>Bless</td>
   </tr>
   <!-- <tr>
      <td>N/A</td>
      <td>Melchizedek</td>
      <td>Pagan Savior</td>
      <td>Justice</td>
      <td>Miniboss</td>
      <td>?</td>
   </tr> -->
</table>

##### 6 - Niijima's Palace - Casino

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>30</td>
      <td>Orlov</td>
      <td>(Treasure Demon)</td>
      <td>Strength</td>
      <td>None</td>
      <td>Curse</td>
   </tr>
   <tr>
      <td>39</td>
      <td>Unicorn</td>
      <td>Expressionless Beast</td>
      <td>Faith</td>
      <td>Timid</td>
      <td>Curse</td>
   </tr>
   <tr>
      <td>40</td>
      <td>Kikuri-Hime</td>
      <td>Mountain Girl</td>
      <td>Priestess</td>
      <td>Timid</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>41</td>
      <td>Power</td>
      <td>Divine Warrior</td>
      <td>Justice</td>
      <td>Irritable</td>
      <td>Curse</td>
   </tr>
   <tr>
      <td>42</td>
      <td>Kushinada</td>
      <td>Lamenting Sacrifice</td>
      <td>Lovers</td>
      <td>Gloomy</td>
      <td>Ice, Nuke</td>
   </tr>
   <tr>
      <td>42</td>
      <td>Ose</td>
      <td>Cruel Leopard</td>
      <td>Fool</td>
      <td>Irritable</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>43</td>
      <td>Queen Mab</td>
      <td>Midnight Queen</td>
      <td>Magician</td>
      <td>Gloomy</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>44</td>
      <td>Valkyrie</td>
      <td>Funerary Warrior</td>
      <td>Strength</td>
      <td>Irritable</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>48</td>
      <td>Rangda</td>
      <td>Dancing Witch</td>
      <td>Magician</td>
      <td>Gloomy</td>
      <td>Elec, Bless</td>
   </tr>
   <tr>
      <td>51</td>
      <td>Jatayu <span class="badge badge-danger">Royal</span></td>
      <td>Arrogant Vulture</td>
      <td>Hanged Man</td>
      <td>Upbeat</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>52</td>
      <td>Norn</td>
      <td>Final Assessor</td>
      <td>Fortune</td>
      <td>Upbeat</td>
      <td>None</td>
   </tr>
   <tr>
      <td>53</td>
      <td>Ganesha</td>
      <td>Auspicious Pachyderm</td>
      <td>Sun</td>
      <td>Upbeat</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>53</td>
      <td>Skadi</td>
      <td>Quaking Lady of Shadow</td>
      <td>Priestess</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <!-- <tr>
      <td>N/A</td>
      <td>Ose</td>
      <td>Cruel Leopard</td>
      <td>Miniboss</td>
      <td>?</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Nebiros</td>
      <td>Wandering Reviver</td>
      <td>Miniboss</td>
      <td>?</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Jatayu</td>
      <td>Arrogant Vulture</td>
      <td>Miniboss</td>
      <td>?</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Norn</td>
      <td>Final Measerer</td>
      <td>Miniboss</td>
      <td>?</td>
      <td>?</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Raja Naga</td>
      <td>Snake King</td>
      <td>Miniboss</td>
      <td>?</td>
      <td>None</td>
   </tr>
   <tr>
      <td>N/A</td>
      <td>Baal</td>
      <td>Reviled Dictator</td>
      <td>Miniboss</td>
      <td>?</td>
      <td>?</td>
   </tr> -->
</table>

##### 7 - Shido's Palace - Ship

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>35</td>
      <td>Emperor's Amulet</td>
      <td>(Treasure Demon)</td>
      <td>Hanged Man</td>
      <td>None</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>48</td>
      <td>Narcissus</td>
      <td>Self-Infatuated Star</td>
      <td>Lovers</td>
      <td>Timid</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>50</td>
      <td>Dakini</td>
      <td>Blood-thirsty Demoness</td>
      <td>Empress</td>
      <td>Upbeat</td>
      <td>None</td>
   </tr>
   <tr>
      <td>50</td>
      <td>Sarasvati</td>
      <td>Strumming Veena Player</td>
      <td>Priestess</td>
      <td>Gloomy</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>52</td>
      <td>Barong</td>
      <td>Dancing Lion</td>
      <td>Emperor</td>
      <td>Upbeat</td>
      <td>Wind, Curse</td>
   </tr>
   <tr>
      <td>52</td>
      <td>Garuda</td>
      <td>Raging Bird God</td>
      <td>Star</td>
      <td>Upbeat</td>
      <td>None</td>
   </tr>
   <tr>
      <td>55</td>
      <td>Cerberus</td>
      <td>Guard Dog of Hades</td>
      <td>Chariot</td>
      <td>Irritable</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>56</td>
      <td>Parvati</td>
      <td>Destructive Beauty</td>
      <td>Lovers</td>
      <td>Timid</td>
      <td>Curse</td>
   </tr>
   <tr>
      <td>56</td>
      <td>Titania</td>
      <td>Scandalous Queen</td>
      <td>Empress</td>
      <td>Upbeat</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>58</td>
      <td>Baphomet</td>
      <td>Heretic Goat</td>
      <td>Devil</td>
      <td>Timid</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>61</td>
      <td>King Frost</td>
      <td>Monarch of Snow</td>
      <td>Emperor</td>
      <td>Upbeat</td>
      <td>None</td>
   </tr>
   <tr>
      <td>63</td>
      <td>Forneus</td>
      <td>Rhetorician of the Sea</td>
      <td>Magician</td>
      <td>Gloomy</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>63</td>
      <td>Kali</td>
      <td>The Blackened Fury</td>
      <td>Empress</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <tr>
      <td>64</td>
      <td>Hanuman</td>
      <td>Nimble Monkey King</td>
      <td>Strength</td>
      <td>Upbeat</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>65</td>
      <td>Atavaka <span class="badge badge-danger">Royal</span></td>
      <td>Infuriated Wisdom King</td>
      <td>Faith</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <tr>
      <td>66</td>
      <td>Oberon</td>
      <td>Unfaithful Dream-King</td>
      <td>Emperor</td>
      <td>Irritable</td>
      <td>Nuke</td>
   </tr>
   
   <!-- <tr>
      <td>N/A</td>
      <td>Ongyo-Ki</td>
      <td>Shadow Cleaner</td>
      <td>Miniboss</td>
      <td>?</td>
      <td>None</td>
   </tr> -->
</table>

##### 8 - Depths of Mementos

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>40</td>
      <td>Hope Diamond</td>
      <td>(Treasure Demon)</td>
      <td>Death</td>
      <td>None</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>58</td>
      <td>Melchizedek</td>
      <td>Pagan Savior</td>
      <td>Justice</td>
      <td>Irritable</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>60</td>
      <td>Lilith</td>
      <td>Harlot of Desire</td>
      <td>Moon</td>
      <td>Timid</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>60</td>
      <td>Moloch</td>
      <td>Sacrificial Pyrekeeper</td>
      <td>Hanged Man</td>
      <td>Upbeat</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>62</td>
      <td>Chernobog</td>
      <td>The Black Avenger</td>
      <td>Death</td>
      <td>Gloomy</td>
      <td>Fire, Bless</td>
   </tr>
   <tr>
      <td>64</td>
      <td>Thor</td>
      <td>Thunder Emperor</td>
      <td>Chariot</td>
      <td>Upbeat</td>
      <td>None</td>
   </tr>
   <tr>
      <td>64</td>
      <td>Yamata-no-Orochi</td>
      <td>Drunken Serpents</td>
      <td>Judgement</td>
      <td>Gloomy</td>
      <td>None</td>
   </tr>
   <tr>
      <td>75</td>
      <td>Abaddon</td>
      <td>Abyssal King of Avarice</td>
      <td>Judgement</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <!-- <tr>
      <td>?</td>
      <td>Dominion</td>
      <td>Merciless Inquisitor</td>
      <td>Justice</td>
      <td>Miniboss</td>
      <td>Elec</td>
   </tr> 
   <tr>
      <td>?</td>
      <td>Throne</td>
      <td>Fire Assassin</td>
      <td>Justice</td>
      <td>Miniboss</td>
      <td>Nuke</td>
   </tr> -->
</table>

##### Qliphoth World

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>50</td>
      <td>Crystal Skull</td>
      <td>(Treasure Demon)</td>
      <td>Fool</td>
      <td>None</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>68</td>
      <td>Dominion</td>
      <td>Merciless Inquisitor</td>
      <td>Justice</td>
      <td>Timid</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>72</td>
      <td>Mot</td>
      <td>Coffin-borne God</td>
      <td>Death</td>
      <td>Gloomy</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>72</td>
      <td>Throne</td>
      <td>Fire Assassin</td>
      <td>Justice</td>
      <td>Gloomy</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>73</td>
      <td>Mara</td>
      <td>Throbbing King of Desire</td>
      <td>Tower</td>
      <td>Timid</td>
      <td>None</td>
   </tr>
   <!-- <tr>
      <td>?</td>
      <td>Uriel</td>
      <td>Herald of Death</td>
      <td>Justice</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr>
   <tr>
      <td>?</td>
      <td>Raphael</td>
      <td>Cleanser of Heaven</td>
      <td>Lovers</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr>
   <tr>
      <td>?</td>
      <td>Gabriel</td>
      <td>Declarer of Anguish</td>
      <td>Temperance</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr>
   <tr>
      <td>?</td>
      <td>Michael</td>
      <td>Apocalyptic Guide</td>
      <td>Judgement</td>
      <td>Miniboss</td>
      <td>None</td>
   </tr> -->
</table>

##### 9 - Maruki's Palace <span class="badge badge-danger">Royal</span>

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>60</td>
      <td>Orichalcum</td>
      <td>(Treasure Demon)</td>
      <td>Faith</td>
      <td>None</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>65</td>
      <td>Bugs</td>
      <td>Killer Teddy Bear</td>
      <td>Fool</td>
      <td>Irritable</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>70</td>
      <td>Byakhee</td>
      <td>Evil Synthetic Organism</td>
      <td>Moon</td>
      <td>Gloomy</td>
      <td>Ice, Nuke</td>
   </tr>
   <tr>
      <td>70</td>
      <td>Loa</td>
      <td>Dream-Dwelling Skull</td>
      <td>Hermit</td>
      <td>Upbeat</td>
      <td>Psy, Bless</td>
   </tr>
   <tr>
      <td>71</td>
      <td>Dionysus</td>
      <td>Hedonistic Braggart</td>
      <td>Councillor</td>
      <td>Upbeat</td>
      <td>None</td>
   </tr>
   <tr>
      <td>73</td>
      <td>Macabre</td>
      <td>Dancer of Death</td>
      <td>Hanged Man</td>
      <td>Gloomy</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>74</td>
      <td>Chimera</td>
      <td>Deformed Lion God</td>
      <td>Strength</td>
      <td>Upbeat</td>
      <td>Wind, Curse</td>
   </tr>
   <tr>
      <td>74</td>
      <td>Nebiros</td>
      <td>Wandering Reviver</td>
      <td>Devil</td>
      <td>Timid</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>76</td>
      <td>Cu Chulainn</td>
      <td>Brave Spear-Bearer</td>
      <td>Faith</td>
      <td>Irritable</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>77</td>
      <td>Scathach</td>
      <td>The Shadowed One</td>
      <td>Priestess</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <tr>
      <td>81</td>
      <td>Alilat</td>
      <td>Decadent False God</td>
      <td>Empress</td>
      <td>Timid</td>
      <td>Fire, Curse</td>
   </tr>
   <tr>
      <td>82</td>
      <td>Baal</td>
      <td>Reviled Dictator</td>
      <td>Emperor</td>
      <td>Upbeat</td>
      <td>None</td>
   </tr>
   <tr>
      <td>86</td>
      <td>Fafnir</td>
      <td>Evil Voracious Dragon</td>
      <td>Hermit</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <tr>
      <td>84</td>
      <td>Hastur</td>
      <td>Warped Abyss</td>
      <td>Star</td>
      <td>Irritable</td>
      <td>None</td>
   </tr>
   <!-- <tr>
      <td>?</td>
      <td>Belial</td>
      <td>Missionary of Depravity</td>
      <td>Devil</td>
      <td>?</td>
      <td>None</td>
   </tr> -->
</table>

##### Mementos - Path of Qimranut

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>2</td>
      <td>Jack-o'-Lantern</td>
      <td>Crypt-dwelling Pyromaniac</td>
      <td>Magician</td>
      <td>Gloomy</td>
      <td>1</td> 
      <td>Gun, Ice, Wind</td>
   </tr>
   <tr>
      <td>2</td>
      <td>Pixie</td>
      <td>Beguiling Girl</td>
      <td>Lovers</td>
      <td>Timid</td>
      <td>1</td>
      <td>Gun, Ice, Curse</td>
   </tr>
   <tr>
      <td>3</td>
      <td>Mandrake</td>
      <td>Gallows Flower</td>
      <td>Death</td>
      <td>Upbeat</td>
      <td>1</td>
      <td>Fire</td>
   </tr>
      <tr>
      <td>4</td>
      <td>Bicorn</td>
      <td>Dirty Two-horned Beast</td>
      <td>Hermit</td>
      <td>Gloomy</td>
      <td>1</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>9</td>
      <td>Berith</td>
      <td>Brutal Cavalryman</td>
      <td>Hierophant</td>
      <td>Irritable</td>
      <td>1</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>10</td>
      <td>Regent</td>
      <td>(Treasure Demon)</td>
      <td>Emperor</td>
      <td>None</td>
      <td>1</td>
      <td>Psy, Nuke</td>
   </tr>
   <tr>
      <td>10</td>
      <td>Slime</td>
      <td>Viscid Rotting Meat</td>
      <td>Chariot</td>
      <td>Timid</td>
      <td>1</td>
      <td>Fire, Wind</td>
   </tr>
</table>

##### Mementos - Path of Aiyatsbus

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>2</td>
      <td>Jack-o'-Lantern</td>
      <td>Crypt-dwelling Pyromaniac</td>
      <td>Magician</td>
      <td>Gloomy</td>
      <td>1</td>
      <td>Gun, Ice, Wind</td>
   </tr>
   <tr>
      <td>2</td>
      <td>Pixie</td>
      <td>Beguiling Girl</td>
      <td>Lovers</td>
      <td>Timid</td>
      <td>1-3</td>
      <td>Gun, Ice, Curse</td>
   </tr>
   <tr>
      <td>3</td>
      <td>Agathion</td>
      <td>Apprentice in a Jug</td>
      <td>Chariot</td>
      <td>Timid</td>
      <td>2-3</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>3</td>
      <td>Mandrake</td>
      <td>Gallows Flower</td>
      <td>Death</td>
      <td>Upbeat</td>
      <td>1</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>4</td>
      <td>Bicorn</td>
      <td>Dirty Two-horned Beast</td>
      <td>Hermit</td>
      <td>Gloomy</td>
      <td>1-2</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>5</td>
      <td>Incubus</td>
      <td>Bedside Brute</td>
      <td>Devil</td>
      <td>Timid</td>
      <td>2-3, 6</td>
      <td>Gun, Bless</td>
   </tr>
   <tr>
      <td>6</td>
      <td>Kelpie</td>
      <td>Mad Marsh Horse</td>
      <td>Strength</td>
      <td>Upbeat</td>
      <td>2-3</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>6</td>
      <td>Silky</td>
      <td>Troublesome Housemaid</td>
      <td>Priestess</td>
      <td>Gloomy</td>
      <td>2-6</td>
      <td>Fire, Elec</td>
   </tr>
   <tr>
      <td>7</td>
      <td>Succubus</td>
      <td>Twilight Prostitute</td>
      <td>Moon</td>
      <td>Irritable</td>
      <td>5-6</td>
      <td>Gun, Bless</td>
   </tr>
   <tr>
      <td>8</td>
      <td>Obariyon</td>
      <td>Piggyback Demon</td>
      <td>Fool</td>
      <td>Irritable</td>
      <td>3-6</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>9</td>
      <td>Berith</td>
      <td>Brutal Cavalryman</td>
      <td>Hierophant</td>
      <td>Irritable</td>
      <td>5-6</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>10</td>
      <td>Andras</td>
      <td>Menacing Owlman</td>
      <td>Devil</td>
      <td>Timid</td>
      <td>5-6</td>
      <td>Gun, Fire</td>
   </tr>
   <tr>
      <td>10</td>
      <td>Regent</td>
      <td>(Treasure Demon)</td>
      <td>Emperor</td>
      <td>None</td>
      <td>All</td>
      <td>Psy, Nuke</td>
   </tr>
   <tr>
      <td>10</td>
      <td>Slime</td>
      <td>Viscid Rotting Meat</td>
      <td>Chariot</td>
      <td>Timid</td>
      <td>1-3, 6</td>
      <td>Fire, Wind</td>
   </tr>
   <tr>
      <td>11</td>
      <td>Kodama</td>
      <td>Wavering Tree Spirit</td>
      <td>Star</td>
      <td>Upbeat</td>
      <td>1-3</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>16</td>
      <td>Archangel</td>
      <td>Heavenly Punisher</td>
      <td>Justice</td>
      <td>Irritable</td>
      <td>5-6</td>
      <td>Elec, Curse</td>
   </tr>
</table>

##### Mementos - Path of Chemdah

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>9</td>
      <td>Koropokguru</td>
      <td>Leafy Old Man</td>
      <td>Hermit</td>
      <td>Timid</td>
      <td>2-3</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>9</td>
      <td>Hua Po</td>
      <td>Girl of the Hanging Tree</td>
      <td>Hanged Man</td>
      <td>Upbeat</td>
      <td>1-3</td>
      <td>Gun, Ice</td>
   </tr>
   <tr>
      <td>9</td>
      <td>Mokoi</td>
      <td>Night-Walking Warrior</td>
      <td>Death</td>
      <td>Gloomy</td>
      <td>1-4</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>10</td>
      <td>Regent</td>
      <td>(Treasure Demon)</td>
      <td>Emperor</td>
      <td>None</td>
      <td>All</td>
      <td>Psy, Nuke</td>
   </tr>
   <tr>
      <td>11</td>
      <td>Jack Frost</td>
      <td>Mocking Snowman</td>
      <td>Magician</td>
      <td>Timid</td>
      <td>4-6</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>11</td>
      <td>Apsaras</td>
      <td>Waterside Nymph</td>
      <td>Priestess</td>
      <td>Upbeat</td>
      <td>1-4</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>11</td>
      <td>Koppa Tengu</td>
      <td>Foolish Monk</td>
      <td>Temperance</td>
      <td>Upbeat</td>
      <td>6-7</td>
      <td>Ice, Bless</td>
   </tr>
   <tr>
      <td>12</td>
      <td>Onmoraki</td>
      <td>Corpse Bird</td>
      <td>Moon</td>
      <td>Gloomy</td>
      <td>3-4</td>
      <td>Gun, Bless</td>
   </tr>
   <tr>
      <td>13</td>
      <td>Ippon-Datara</td>
      <td>Embittered Blacksmith</td>
      <td>Hermit</td>
      <td>Upbeat</td>
      <td>1-4</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>14</td>
      <td>Inugami</td>
      <td>Possessing Dog Ghost</td>
      <td>Hanged Man</td>
      <td>Timid</td>
      <td>4-7</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>15</td>
      <td>Makami</td>
      <td>Hunting Wolf Spirit</td>
      <td>Temperance</td>
      <td>Upbeat</td>
      <td>6-7</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>16</td>
      <td>Eligor</td>
      <td>War-hungry Horseman</td>
      <td>Emperor</td>
      <td>Irritable</td>
      <td>3-4</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>17</td>
      <td>Sudama</td>
      <td>Noisy Mountain Spirit</td>
      <td>Hermit</td>
      <td>Timid</td>
      <td>6-7</td>
      <td>Ice, Nuke</td>
   </tr>
   <tr>
      <td>20</td>
      <td>Nue</td>
      <td>Night Chimera</td>
      <td>Moon</td>
      <td>Irritable</td>
      <td>4</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>21</td>
      <td>Shiki-Ouji</td>
      <td>Bringer of Misfortune</td>
      <td>Chariot</td>
      <td>Irritable</td>
      <td>6-7</td>
      <td>Nuke</td>
   </tr>
</table>

##### Mementos - Path of Kaitul

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>12</td>
      <td>Angel</td>
      <td>Zealous Messenger</td>
      <td>Justice</td>
      <td>Irritable</td>
      <td>1-4</td>
      <td>Curse</td>
   </tr>
   <tr>
      <td>15</td>
      <td>Queen's Necklace</td>
      <td>(Treasure Demon)</td>
      <td>Justice</td>
      <td>None</td>
      <td>All</td>
      <td>Gun</td>
   </tr>
   <tr>
      <td>16</td>
      <td>High Pixie</td>
      <td>Prankster Leader</td>
      <td>Fool</td>
      <td>Irritable</td>
      <td>1-5</td>
      <td>Gun, Nuke</td>
   </tr>
   <tr>
      <td>17</td>
      <td>Orobas</td>
      <td>Equine Sage</td>
      <td>Hierophant</td>
      <td>Timid</td>
      <td>1-5</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>17</td>
      <td>Nekomata</td>
      <td>Ascended Feline</td>
      <td>Magician</td>
      <td>Upbeat</td>
      <td>2-4</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>19</td>
      <td>Leanan Sidhe</td>
      <td>Jealous Lover</td>
      <td>Lovers</td>
      <td>Irritable</td>
      <td>3-5</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>19</td>
      <td>Oni</td>
      <td>Chivalrous Guard/Chivalrous Fiend</td>
      <td>Strength</td>
      <td>Upbeat</td>
      <td>3-5, 8-9</td>
      <td>None</td>
   </tr>
   <tr>
      <td>20</td>
      <td>Yaksini</td>
      <td>Human-eating Lady</td>
      <td>Empress</td>
      <td>Irritable</td>
      <td>3-7</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>21</td>
      <td>Orthrus</td>
      <td>Twin-headed Guardian</td>
      <td>Hanged Man</td>
      <td>Irritable</td>
      <td>4-9</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>23</td>
      <td>Fuu-ki</td>
      <td>Tornado Devil</td>
      <td>Star</td>
      <td>Gloomy</td>
      <td>8-9</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>24</td>
      <td>Sui-ki</td>
      <td>Floodbringer Demon</td>
      <td>Moon</td>
      <td>Gloomy</td>
      <td>7-9</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>24</td>
      <td>Rakshasa</td>
      <td>Battle Fiend</td>
      <td>Strength</td>
      <td>Irritable</td>
      <td>5-9</td>
      <td>Wind, Bless</td>
   </tr>
   <tr>
      <td>25</td>
      <td>Kin-ki</td>
      <td>Demonic Warlord</td>
      <td>Chariot</td>
      <td>Gloomy</td>
      <td>9</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>28</td>
      <td>Choronzon</td>
      <td>Gathering Devil</td>
      <td>Magician</td>
      <td>Timid</td>
      <td>1-5</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>29</td>
      <td>Take-Minakata</td>
      <td>Defeated Avenger</td>
      <td>Hanged Man</td>
      <td>Gloomy</td>
      <td>7-9</td>
      <td>Psy</td>
   </tr>
</table>

##### Mementos - Path of Akzeriyyuth

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>20</td>
      <td>Stone of Scone</td>
      <td>(Treasure Demon)</td>
      <td>Fortune</td>
      <td>None</td>
      <td>All</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>24</td>
      <td>Sandman</td>
      <td>Envoy of Slumber</td>
      <td>Magician</td>
      <td>Irritable</td>
      <td>1-3</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>24</td>
      <td>Naga</td>
      <td>Cavern Snakeman</td>
      <td>Hermit</td>
      <td>Gloomy</td>
      <td>2-9</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>25</td>
      <td>Anzu</td>
      <td>Thief of Tablets</td>
      <td>Hierophant</td>
      <td>Irritable</td>
      <td>1-11</td>
      <td>Gun, Nuke</td>
   </tr>
   <tr>
      <td>26</td>
      <td>Isis</td>
      <td>She of Life and Death</td>
      <td>Priestess</td>
      <td>Timid</td>
      <td>5-11</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>26</td>
      <td>Lamia</td>
      <td>Slithering Snakewoman</td>
      <td>Empress</td>
      <td>Gloomy</td>
      <td>3-11</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>29</td>
      <td>Pisaca</td>
      <td>Corpse-eating Corpse</td>
      <td>Death</td>
      <td>Gloomy</td>
      <td>5, 7, 9, 11</td>
      <td>Fire, Bless</td>
   </tr>
   <tr>
      <td>36</td>
      <td>Thoth</td>
      <td>Chanting Baboon</td>
      <td>Emperor</td>
      <td>Gloomy</td>
      <td>6-11</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>37</td>
      <td>Anubis</td>
      <td>Bearer of the Scales</td>
      <td>Judgement</td>
      <td>Gloomy</td>
      <td>10-11</td>
      <td>None</td>
   </tr>
</table>

##### Mementos - Path of Adyeshach

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>25</td>
      <td>Koh-i-Noor</td>
      <td>(Treasure Demon)</td>
      <td>Priestess</td>
      <td>None</td>
      <td>All</td>
      <td>None</td>
   </tr>
   <tr>
      <td>29</td>
      <td>Black Ooze</td>
      <td>Pulsing Mud</td>
      <td>Moon</td>
      <td>Irritable</td>
      <td>1-6</td>
      <td>Elec, Psy, Bless</td>
   </tr>
   <tr>
      <td>32</td>
      <td>Decarabia</td>
      <td>Vicious Pentagram</td>
      <td>Fool</td>
      <td>Gloomy</td>
      <td>3-8</td>
      <td>Phys</td>
   </tr>
   <tr>
      <td>32</td>
      <td>Lilim</td>
      <td>Woman Who Brings Ruin</td>
      <td>Devil</td>
      <td>Gloomy</td>
      <td>6-12</td>
      <td>Gun, Wind, Bless</td>
   </tr>
   <tr>
      <td>33</td>
      <td>Mothman</td>
      <td>Vampire Moth</td>
      <td>Moon</td>
      <td>Timid</td>
      <td>3-4, 7-10</td>
      <td>Gun</td>
   </tr>
   <tr>
      <td>35</td>
      <td>Arahabaki</td>
      <td>Awakened God</td>
      <td>Hermit</td>
      <td>Gloomy</td>
      <td>1-10</td>
      <td>Psy, Nuke</td>
   </tr>
   <tr>
      <td>36</td>
      <td>Kaiwan</td>
      <td>Wishless Star</td>
      <td>Star</td>
      <td>Timid</td>
      <td>10-12</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>37</td>
      <td>Belphegor</td>
      <td>Ambassador of Filth</td>
      <td>Tower</td>
      <td>Irritable</td>
      <td>6-10</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>38</td>
      <td>Legion</td>
      <td>Fused Ghost</td>
      <td>Fool</td>
      <td>Upbeat</td>
      <td>1-2, 4</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>39</td>
      <td>Mithras</td>
      <td>Dark Sun</td>
      <td>Sun</td>
      <td>Gloomy</td>
      <td>11-12</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>44</td>
      <td>Girimehkala</td>
      <td>Rebellious Elephant</td>
      <td>Moon</td>
      <td>Gloomy</td>
      <td>4-10</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>45</td>
      <td>Scathach</td>
      <td>The Shadowed One</td>
      <td>Priestess</td>
      <td>Upbeat</td>
      <td>10-12</td>
      <td>None</td>
   </tr>
</table>

##### Mementos - Path of Sheriruth 1-5

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>30</td>
      <td>Orlov</td>
      <td>(Treasure Demon)</td>
      <td>Strength</td>
      <td>None</td>
      <td>1-5</td>
      <td>Curse</td>
   </tr>
   <tr>
      <td>39</td>
      <td>Unicorn</td>
      <td>Expressionless Beast</td>
      <td>Hierophant</td>
      <td>Timid</td>
      <td>1-2</td>
      <td>Curse</td>
   </tr>
   <tr>
      <td>40</td>
      <td>Kikuri-Hime</td>
      <td>Mountain Girl</td>
      <td>Priestess</td>
      <td>Gloomy</td>
      <td>2-3</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>41</td>
      <td>Power</td>
      <td>Divine Warrior</td>
      <td>Justice</td>
      <td>Irritable</td>
      <td>1-3</td>
      <td>Gun, Curse</td>
   </tr>
   <tr>
      <td>42</td>
      <td>Ose</td>
      <td>Cruel Leopard</td>
      <td>Fool</td>
      <td>Upbeat</td>
      <td>1-4</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>42</td>
      <td>Kushinada</td>
      <td>Lamenting Sacrifice</td>
      <td>Lovers</td>
      <td>Upbeat</td>
      <td>3-4</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>42</td>
      <td>Kumbhanda</td>
      <td>Life-Draining Spirit</td>
      <td>Hermit</td>
      <td>Irritable</td>
      <td>4-5</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>43</td>
      <td>Queen Mab</td>
      <td>Midnight Queen</td>
      <td>Magician</td>
      <td>Gloomy</td>
      <td>3-4</td>
      <td>Wind</td>
   </tr>
   <tr>
      <td>44</td>
      <td>Valkyrie</td>
      <td>Funerary Warrior</td>
      <td>Strength</td>
      <td>Irritable</td>
      <td>2-4</td>
      <td>None</td>
   </tr>
   <tr>
      <td>48</td>
      <td>Rangda</td>
      <td>Dancing Witch</td>
      <td>Magician</td>
      <td>Gloomy</td>
      <td>5</td>
      <td>Elec, Bless</td>
   </tr>
   <tr>
      <td>52</td>
      <td>Norn</td>
      <td>Final Measerer</td>
      <td>Fortune</td>
      <td>Upbeat</td>
      <td>5</td>
      <td>None</td>
   </tr>
   <tr>
      <td>53</td>
      <td>Ganesha</td>
      <td>Auspicious Pachyderm</td>
      <td>Sun</td>
      <td>Upbeat</td>
      <td>3-4</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>55</td>
      <td>Skadi</td>
      <td>Quaking Lady of Shadow</td>
      <td>Priestess</td>
      <td>Timid</td>
      <td>5</td>
      <td>None</td>
   </tr>
</table>

##### Mementos - Path of Sheriruth 7-13

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <tr>
      <td>35</td>
      <td>Emperor's Amulet</td>
      <td>(Treasure Demon)</td>
      <td>Hanged Man</td>
      <td>None</td>
      <td>7-13</td>
      <td>Elec</td>
   </tr> 
   <tr>
      <td>40</td>
      <td>Hope Diamond</td>
      <td>(Treasure Demon)</td>
      <td>Death</td>
      <td>None</td>
      <td>7-13</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>50</td>
      <td>Crystal Skull</td>
      <td>(Treasure Demon)</td>
      <td>Fool</td>
      <td>None</td>
      <td>7-13</td>
      <td>None</td>
   </tr>
   <tr>
      <td>50</td>
      <td>Dakini</td>
      <td>Blood-thirsty Demoness</td>
      <td>Empress</td>
      <td>Upbeat</td>
      <td>7-9</td>
      <td>None</td>
   </tr> 
   <tr>
      <td>50</td>
      <td>Sarasvati</td>
      <td>Strumming Veena Player</td>
      <td>Priestess</td>
      <td>Timid</td>
      <td>7-9, 12</td>
      <td>Nuke</td>
   </tr>
   <tr>
      <td>50</td>
      <td>Narcissus</td>
      <td>Self-Infatuated Star</td>
      <td>Lovers</td>
      <td>Timid</td>
      <td>7-8</td>
      <td>Fire</td>
   </tr>
   <tr>
      <td>52</td>
      <td>Barong</td>
      <td>Dancing Lion</td>
      <td>Emperor</td>
      <td>Upbeat</td>
      <td>11-12</td>
      <td>Wind, Curse</td>
   </tr>
   <tr>
      <td>52</td>
      <td>Garuda</td>
      <td>Raging Bird God</td>
      <td>Star</td>
      <td>Upbeat</td>
      <td>12</td>
      <td>Gun</td>
   </tr>
   <tr>
      <td>55</td>
      <td>Cerberus</td>
      <td>Guard Dog of Hades</td>
      <td>Chariot</td>
      <td>Irritable</td>
      <td>7-9</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>56</td>
      <td>Titania</td>
      <td>Scandalous Queen</td>
      <td>Empress</td>
      <td>Timid</td>
      <td>8-13</td>
      <td>Psy</td>
   </tr>
   <tr>
      <td>56</td>
      <td>Parvati</td>
      <td>Destructive Beauty</td>
      <td>Lovers</td>
      <td>Timid</td>
      <td>9-12</td>
      <td>Curse</td>
   </tr>
   <tr>
      <td>56</td>
      <td>Kurama Tengu</td>
      <td>Monk of the Valley</td>
      <td>Hermit</td>
      <td>Irritable</td>
      <td>11-12</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>58</td>
      <td>Baphomet</td>
      <td>Heretic Goat</td>
      <td>Devil</td>
      <td>Timid</td>
      <td>13</td>
      <td>Bless</td>
   </tr>
   <tr>
      <td>61</td>
      <td>King Frost</td>
      <td>Monarch of Snow</td>
      <td>Emperor</td>
      <td>Upbeat</td>
      <td>8, 11-13</td>
      <td>None</td>
   </tr>
   <tr>
      <td>63</td>
      <td>Forneus</td>
      <td>Rhetorician of the Sea</td>
      <td>Hierophant</td>
      <td>Timid</td>
      <td>12-13</td>
      <td>Elec</td>
   </tr>
   <tr>
      <td>64</td>
      <td>Hanuman</td>
      <td>Nimble Monkey King</td>
      <td>Star</td>
      <td>Upbeat</td>
      <td>12-13</td>
      <td>Ice</td>
   </tr>
   <tr>
      <td>66</td>
      <td>Oberon</td>
      <td>Unfaithful Dream-King</td>
      <td>Emperor</td>
      <td>Irritable</td>
      <td>13</td>
      <td>Nuke</td>
   </tr>
</table>

##### Mementos - Path of Da'at <span class="badge badge-danger">Royal</span>

<table class='table-responsive-sm'>
   <tr>
      <th>Level</th>
      <th>Persona</th>
      <th>Shadow</th>
      <th>Arcana</th>
      <th>Personality</th>
      <th>Areas</th>
      <th>Weakness</th>
   </tr>
   <!-- <tr>
      <td>35</td>
      <td>Emperor's Amulet</td>
      <td>(Treasure Demon)</td>
      <td>Hanged Man</td>
      <td>None</td>
      <td>7-13</td>
      <td>Elec</td>
   </tr>  -->
</table>