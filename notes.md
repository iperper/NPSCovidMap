## National Parks COVID

All Information at Bottom Waste of Time: NPS has an API!

curl -X GET "https://developer.nps.gov/api/v1/alerts?parkCode=&stateCode=CA&limit=10&start=1&api_key=IvUo9pRS4hduNe23QLYadtXjRXC58DUh4vkTaftl" -H "accept: application/json"

Have no arguments to get everything





Active Alerts Page looks like this:
https://www.nps.gov/planyourvisit/alerts.htm?&p=1&v=0

Note we filter by closures:
https://www.nps.gov/planyourvisit/alerts.htm?t=Closure&p=1&v=0

Page two:
https://www.nps.gov/planyourvisit/alerts.htm?t=Closure&p=2&v=0


With all filters:

https://www.nps.gov/planyourvisit/alerts.htm?s=AK&pk=anch&t=Closure&p=1&v=0


Looks like:

s="state"?pk="park id"?t="alert type"?p="page number"?v="unknown"


State Selector:
```html
<select id="form-state" class="form-control SingleSelect" data-nonselectedtext="State" data-enablefiltering="true" data-keeper-edited="yes">
<option value="" disabled="" selected="">State</option>
<option value="AL">Alabama</option>
<option value="AK">Alaska</option>
<option value="AS">American Samoa</option>
<option value="AZ">Arizona</option>
<option value="AR">Arkansas</option>
<option value="CA">California</option>
<option value="CO">Colorado</option>
<option value="CT">Connecticut</option>
<option value="DE">Delaware</option>
<option value="DC">District of Columbia</option>
<option value="FL">Florida</option>
<option value="GA">Georgia</option>
<option value="GU">Guam</option>
<option value="HI">Hawaii</option>
<option value="ID">Idaho</option>
<option value="IL">Illinois</option>
<option value="IN">Indiana</option>
<option value="IA">Iowa</option>
<option value="KS">Kansas</option>
<option value="KY">Kentucky</option>
<option value="LA">Louisiana</option>
<option value="ME">Maine</option>
<option value="MD">Maryland</option>
<option value="MA">Massachusetts</option>
<option value="MI">Michigan</option>
<option value="MN">Minnesota</option>
<option value="MS">Mississippi</option>
<option value="MO">Missouri</option>
<option value="MT">Montana</option>
<option value="NE">Nebraska</option>
<option value="NV">Nevada</option>
<option value="NH">New Hampshire</option>
<option value="NJ">New Jersey</option>
<option value="NM">New Mexico</option>
<option value="NY">New York</option>
<option value="NC">North Carolina</option>
<option value="ND">North Dakota</option>
<option value="MP">Northern Mariana Islands</option>
<option value="OH">Ohio</option>
<option value="OK">Oklahoma</option>
<option value="OR">Oregon</option>
<option value="PA">Pennsylvania</option>
<option value="PR">Puerto Rico</option>
<option value="RI">Rhode Island</option>
<option value="SC">South Carolina</option>
<option value="SD">South Dakota</option>
<option value="TN">Tennessee</option>
<option value="TX">Texas</option>
<option value="UT">Utah</option>
<option value="VT">Vermont</option>
<option value="VI">Virgin Islands</option>
<option value="VA">Virginia</option>
<option value="WA">Washington</option>
<option value="WV">West Virginia</option>
<option value="WI">Wisconsin</option>
<option value="WY">Wyoming</option>
</select>
```


Closure Type Selector:
```html
<select id="form-type" class="Multiselect js-multiselect" data-nonselectedtext="Alert Type" multiple="multiple" style="display: none;">
<option value="Danger">Danger</option>
<option value="Closure">Closure</option>
<option value="Caution">Caution</option>
<option value="Information">Information</option>
</select>
```

The Park Selector is a dropdown menu, where checkboxes produce value codes for a given park:

```html
<ul class="multiselect-container dropdown-menu" style="max-height: 300px; overflow: hidden auto;"><li><a href="javascript:void(0);" id="anch_13"><label class="checkbox"><input type="checkbox" value="abli"> Abraham Lincoln Birthplace National Historical Park</label></a></li><li><a href="javascript:void(0);" id="anch_14"><label class="checkbox"><input type="checkbox" value="acad"> Acadia National Park</label></a></li>
```


```python
{
    "abli":"Abraham Lincoln Birthplace National Historical Park",
    "acad":"Acadia National Park",
    "adam":"Adams National Historical Park",
    "afam":"African American Civil War Memorial",
    "afbg":"African Burial Ground National Monument",
    "agfo":"Agate Fossil Beds National Monument",
    "alka":"Ala Kahakai National Historic Trail",
    "alag":"Alagnak Wild River",
    "anch":"Alaska Public Lands",
    "alca":"Alcatraz Island ",
    "aleu":"Aleutian Islands World War II National Historic Area",
    "alfl":"Alibates Flint Quarries National Monument",
    "alpo":"Allegheny Portage Railroad National Historic Site",
    "amme":"American Memorial Park",
    "amis":"Amistad National Recreation Area",
    "anac":"Anacostia Park",
    "ande":"Andersonville National Historic Site",
    "anjo":"Andrew Johnson National Historic Site",
    "ania":"Aniakchak National Monument & Preserve",
    "anti":"Antietam National Battlefield",
    "apis":"Apostle Islands National Lakeshore",
    "appa":"Appalachian National Scenic Trail",
    "apco":"Appomattox Court House National Historical Park",
    "arch":"Arches National Park",
    "arpo":"Arkansas Post National Memorial",
    "arho":"Arlington House, The Robert  E. Lee Memorial",
    "asis":"Assateague Island National Seashore",
    "auca":"Augusta Canal National Heritage Area",
    "azru":"Aztec Ruins National Monument",
    "badl":"Badlands National Park",
    "balt":"Baltimore National Heritage Area",
    "bawa":"Baltimore-Washington Parkway",
    "band":"Bandelier National Monument",
    "bepa":"Belmont-Paul Women's Equality National Monument",
    "beol":"Bent's Old Fort National Historic Site",
    "bela":"Bering Land Bridge National Preserve",
    "bibe":"Big Bend National Park",
    "bicy":"Big Cypress National Preserve",
    "biho":"Big Hole National Battlefield",
    "biso":"Big South Fork National River & Recreation Area",
    "bith":"Big Thicket National Preserve",
    "bica":"Bighorn Canyon National Recreation Area",
    "bicr":"Birmingham Civil Rights National Monument",
    "bisc":"Biscayne National Park",
    "blca":"Black Canyon Of The Gunnison National Park",
    "blrv":"Blackstone River Valley National Historical Park",
    "blri":"Blue Ridge Parkway",
    "blrn":"Blue Ridge National Heritage Area",
    "blue":"Bluestone National Scenic River",
    "bowa":"Booker T Washington National Monument",
    "bost":"Boston National Historical Park",
    "boaf":"Boston African American National Historic Site",
    "boha":"Boston Harbor Islands National Recreation Area",
    "brcr":"Brices Cross Roads National Battlefield Site",
    "brvb":"Brown v. Board of Education National Historic Site",
    "brca":"Bryce Canyon National Park",
    "buis":"Buck Island Reef National Monument",
    "buff":"Buffalo National River",
    "cabr":"Cabrillo National Monument",
    "cali":"California National Historic Trail",
    "cane":"Camp Nelson National Monument",
    "cana":"Canaveral National Seashore",
    "crha":"Cane River National Heritage Area",
    "cari":"Cane River Creole National Historical Park",
    "cach":"Canyon de Chelly National Monument",
    "cany":"Canyonlands National Park",
    "caco":"Cape Cod National Seashore",
    "caha":"Cape Hatteras National Seashore",
    "came":"Cape Henry Memorial Part of Colonial National Historical Park",
    "cakr":"Cape Krusenstern National Monument",
    "calo":"Cape Lookout National Seashore",
    "cahi":"Capitol Hill Parks ",
    "care":"Capitol Reef National Park",
    "cajo":"Captain John Smith Chesapeake National Historic Trail",
    "cavo":"Capulin Volcano National Monument",
    "carl":"Carl Sandburg Home National Historic Site",
    "cave":"Carlsbad Caverns National Park",
    "cawo":"Carter G. Woodson Home National Historic Site",
    "cagr":"Casa Grande Ruins National Monument",
    "casa":"Castillo de San Marcos National Monument",
    "cacl":"Castle Clinton National Monument",
    "camo":"Castle Mountains National Monument",
    "cato":"Catoctin Mountain Park",
    "cebr":"Cedar Breaks National Monument",
    "cebe":"Cedar Creek & Belle Grove National Historical Park",
    "chcu":"Chaco Culture National Historical Park",
    "cham":"Chamizal National Memorial",
    "chis":"Channel Islands National Park",
    "chpi":"Charles Pinckney National Historic Site",
    "chyo":"Charles Young Buffalo Soldiers National Monument",
    "chat":"Chattahoochee River National Recreation Area",
    "choh":"Chesapeake & Ohio Canal National Historical Park",
    "cbpo":"Chesapeake Bay ",
    "chch":"Chickamauga & Chattanooga National Military Park",
    "chic":"Chickasaw National Recreation Area",
    "chir":"Chiricahua National Monument",
    "chri":"Christiansted National Historic Site",
    "ciro":"City Of Rocks National Reserve",
    "cwdw":"Civil War Defenses of Washington ",
    "clba":"Clara Barton National Historic Site",
    "coal":"Coal National Heritage Area",
    "colo":"Colonial National Historical Park",
    "colm":"Colorado National Monument",
    "cong":"Congaree National Park",
    "coga":"Constitution Gardens ",
    "coro":"Coronado National Memorial",
    "cowp":"Cowpens National Battlefield",
    "crla":"Crater Lake National Park",
    "crmo":"Craters Of The Moon National Monument & Preserve",
    "xrds":"Crossroads of the American Revolution National Heritage Area"
    "cuga":"Cumberland Gap National Historical Park",
    "cuis":"Cumberland Island National Seashore",
    "cure":"Curecanti National Recreation Area",
    "cuva":"Cuyahoga Valley National Park",
    "dabe":"David Berger National Memorial",
    "daav":"Dayton Aviation Heritage National Historical Park",
    "deso":"De Soto National Memorial",
    "deva":"Death Valley National Park",
    "dele":"Delaware & Lehigh National Heritage Corridor",
    "dewa":"Delaware Water Gap National Recreation Area",
    "dena":"Denali National Park & Preserve",
    "depo":"Devils Postpile National Monument",
    "deto":"Devils Tower National Monument",
    "dino":"Dinosaur National Monument",
    "drto":"Dry Tortugas National Park",
    "ebla":"Ebey's Landing National Historical Reserve",
    "edal":"Edgar Allan Poe National Historic Site",
    "efmo":"Effigy Mounds National Monument",
    "eise":"Eisenhower National Historic Site",
    "elte":"El Camino Real de los Tejas National Historic Trail",
    "elca":"El Camino Real de Tierra Adentro National Historic Trail"
    "elma":"El Malpais National Monument",
    "elmo":"El Morro National Monument",
    "elro":"Eleanor Roosevelt National Historic Site",
    "elis":"Ellis Island Part of Statue of Liberty National Monument"
    "erie":"Erie Canalway National Heritage Corridor",
    "esse":"Essex National Heritage Area",
    "euon":"Eugene O'Neill National Historic Site",
    "ever":"Everglades National Park",
    "fati":"Fallen Timbers Battlefield and Fort Miamis National Historic Site",
    "feha":"Federal Hall National Memorial",
    "fiis":"Fire Island National Seashore",
    "fila":"First Ladies National Historic Site",
    "frst":"First State National Historical Park",
    "flni":"Flight 93 National Memorial",
    "flfo":"Florissant Fossil Beds National Monument",
    "foth":"Ford's Theatre ",
    "fobo":"Fort Bowie National Historic Site",
    "foca":"Fort Caroline National Memorial",
    "foda":"Fort Davis National Historic Site",
    "fodo":"Fort Donelson National Battlefield",
    "fodu":"Fort Dupont Park ",
    "fofo":"Fort Foote Park",
    "fofr":"Fort Frederica National Monument",
    "fola":"Fort Laramie National Historic Site",
    "fols":"Fort Larned National Historic Site",
    "foma":"Fort Matanzas National Monument",
    "fomc":"Fort McHenry National Monument and Historic Shrine",
    "fomr":"Fort Monroe National Monument",
    "fone":"Fort Necessity National Battlefield",
    "fopo":"Fort Point National Historic Site",
    "fopu":"Fort Pulaski National Monument",
    "fora":"Fort Raleigh National Historic Site",
    "fosc":"Fort Scott National Historic Site",
    "fosm":"Fort Smith National Historic Site",
    "fost":"Fort Stanwix National Monument",
    "fosu":"Fort Sumter and Fort Moultrie National Historical Park"
    "foun":"Fort Union National Monument",
    "fous":"Fort Union Trading Post National Historic Site",
    "fova":"Fort Vancouver National Historic Site",
    "fowa":"Fort Washington Park",
    "fobu":"Fossil Butte National Monument",
    "frde":"Franklin Delano Roosevelt Memorial ",
    "frdo":"Frederick Douglass National Historic Site",
    "frla":"Frederick Law Olmsted National Historic Site",
    "frsp":"Fredericksburg & Spotsylvania National Military Park",
    "frri":"Freedom Riders National Monument",
    "frhi":"Friendship Hill National Historic Site",
    "gaar":"Gates Of The Arctic National Park & Preserve",
    "gate":"Gateway National Recreation Area",
    "jeff":"Gateway Arch National Park",
    "gari":"Gauley River National Recreation Area",
    "gegr":"General Grant National Memorial",
    "gero":"George Rogers Clark National Historical Park",
    "gwmp":"George Washington Memorial Parkway",
    "gewa":"George Washington Birthplace National Monument",
    "gwca":"George Washington Carver National Monument",
    "gett":"Gettysburg National Military Park",
    "gicl":"Gila Cliff Dwellings National Monument",
    "glac":"Glacier National Park",
    "glba":"Glacier Bay National Park & Preserve",
    "glca":"Glen Canyon National Recreation Area",
    "glec":"Glen Echo Park",
    "glde":"Gloria Dei Church National Historic Site",
    "goga":"Golden Gate National Recreation Area",
    "gosp":"Golden Spike National Historical Park",
    "gois":"Governors Island National Monument",
    "grca":"Grand Canyon National Park",
    "grpo":"Grand Portage National Monument",
    "grte":"Grand Teton National Park",
    "grko":"Grant-Kohrs Ranch National Historic Site",
    "grba":"Great Basin National Park",
    "greg":"Great Egg Harbor River ",
    "grfa":"Great Falls Park",
    "grsa":"Great Sand Dunes National Park & Preserve",
    "grsm":"Great Smoky Mountains National Park",
    "grsp":"Green Springs ",
    "gree":"Greenbelt Park",
    "gumo":"Guadalupe Mountains National Park",
    "guco":"Guilford Courthouse National Military Park",
    "guis":"Gulf Islands National Seashore",
    "guge":"Gullah/Geechee Cultural Heritage Corridor",
    "hafo":"Hagerman Fossil Beds National Monument",
    "hale":"Haleakalā National Park",
    "hagr":"Hamilton Grange National Memorial",
    "hamp":"Hampton National Historic Site",
    "haha":"Harmony Hall ",
    "hafe":"Harpers Ferry National Historical Park",
    "hart":"Harriet Tubman National Historical Park",
    "hatu":"Harriet Tubman Underground Railroad National Historical Park"
    "hstr":"Harry S Truman National Historic Site",
    "havo":"Hawai'i Volcanoes National Park",
    "heho":"Herbert Hoover National Historic Site",
    "jame":"Historic Jamestowne Part of Colonial National Historical Park",
    "hofr":"Home Of Franklin D Roosevelt National Historic Site",
    "home":"Homestead National Monument of America",
    "hono":"Honouliuli National Historic Site",
    "hocu":"Hopewell Culture National Historical Park",
    "hofu":"Hopewell Furnace National Historic Site",
    "hobe":"Horseshoe Bend National Military Park",
    "hosp":"Hot Springs National Park",
    "hove":"Hovenweep National Monument",
    "hutr":"Hubbell Trading Post National Historic Site",
    "hurv":"Hudson River Valley National Heritage Area",
    "inup":"Iñupiat Heritage Center ",
    "iatr":"Ice Age National Scenic Trail",
    "iafl":"Ice Age Floods National Geologic Trail",
    "inde":"Independence National Historical Park",
    "indu":"Indiana Dunes National Park",
    "isro":"Isle Royale National Park",
    "jaga":"James A Garfield National Historic Site",
    "jela":"Jean Lafitte National Historical Park and Preserve",
    "jeca":"Jewel Cave National Monument",
    "jica":"Jimmy Carter National Historic Site",
    "joda":"John Day Fossil Beds National Monument",
    "jofi":"John Fitzgerald Kennedy National Historic Site",
    "blac":"John H. Chafee Blackstone River Valley National Heritage Corridor",
    "jomu":"John Muir National Historic Site",
    "jofl":"Johnstown Flood National Memorial",
    "jotr":"Joshua Tree National Park",
    "juba":"Juan Bautista de Anza National Historic Trail",
    "kala":"Kalaupapa National Historical Park",
    "kaho":"Kaloko-Honokōhau National Historical Park",
    "kaww":"Katahdin Woods and Waters National Monument",
    "katm":"Katmai National Park & Preserve",
    "kefj":"Kenai Fjords National Park",
    "keaq":"Kenilworth Park & Aquatic Gardens ",
    "kemo":"Kennesaw Mountain National Battlefield Park",
    "kewe":"Keweenaw National Historical Park",
    "kimo":"Kings Mountain National Military Park",
    "klgo":"Klondike Gold Rush National Historical Park",
    "klse":"Klondike Gold Rush - Seattle Unit National Historical Park",
    "knri":"Knife River Indian Villages National Historic Site",
    "kova":"Kobuk Valley National Park",
    "kowa":"Korean War Veterans Memorial ",
    "lacl":"Lake Clark National Park & Preserve",
    "lake":"Lake Mead National Recreation Area",
    "lamr":"Lake Meredith National Recreation Area",
    "laro":"Lake Roosevelt National Recreation Area",
    "lavo":"Lassen Volcanic National Park",
    "labe":"Lava Beds National Monument",
    "lyba":"LBJ Memorial Grove on the Potomac ",
    "lecl":"Lewis & Clark National Historic Trail",
    "lewi":"Lewis and Clark National Historical Park",
    "libo":"Lincoln Boyhood National Memorial",
    "liho":"Lincoln Home National Historic Site",
    "linc":"Lincoln Memorial ",
    "libi":"Little Bighorn Battlefield National Monument",
    "liri":"Little River Canyon National Preserve",
    "chsc":"Little Rock Central High School National Historic Site",
    "long":"Longfellow House Washington's Headquarters National Historic Site",
    "lowe":"Lowell National Historical Park",
    "lode":"Lower Delaware National Wild and Scenic River",
    "loea":"Lower East Side Tenement Museum National Historic Site",
    "lyjo":"Lyndon B Johnson National Historical Park",
    "mawa":"Maggie L Walker National Historic Site",
    "maac":"Maine Acadian Culture ",
    "maca":"Mammoth Cave National Park",
    "mana":"Manassas National Battlefield Park",
    "mapr":"Manhattan Project National Historical Park",
    "manz":"Manzanar National Historic Site",
    "mabi":"Marsh - Billings - Rockefeller National Historical Park",
    "malu":"Martin Luther King, Jr. National Historical Park",
    "mlkm":"Martin Luther King, Jr. Memorial ",
    "mava":"Martin Van Buren National Historic Site",
    "mamc":"Mary McLeod Bethune Council House National Historic Site",
    "meve":"Mesa Verde National Park",
    "miin":"Minidoka National Historic Site",
    "mima":"Minute Man National Historical Park",
    "mimi":"Minuteman Missile National Historic Site",
    "miss":"Mississippi National River and Recreation Area",
    "mnrr":"Missouri National Recreational River",
    "moja":"Mojave National Preserve",
    "mono":"Monocacy National Battlefield",
    "moca":"Montezuma Castle National Monument",
    "mocr":"Moores Creek National Battlefield",
    "mopi":"Mormon Pioneer National Historic Trail",
    "morr":"Morristown National Historical Park",
    "auto":"Motor Cities National Heritage Area",
    "mora":"Mount Rainier National Park",
    "moru":"Mount Rushmore National Memorial",
    "muwo":"Muir Woods National Monument",
    "natc":"Natchez National Historical Park",
    "natr":"Natchez Trace Parkway",
    "natt":"Natchez Trace National Scenic Trail",
    "avia":"National Aviation Heritage Area",
    "nace":"National Capital Parks-East ",
    "nama":"National Mall and Memorial Parks ",
    "npsa":"National Park of American Samoa ",
    "npnh":"National Parks of New York Harbor ",
    "nabr":"Natural Bridges National Monument",
    "nava":"Navajo National Monument",
    "nebe":"New Bedford Whaling National Historical Park",
    "neen":"New England National Scenic Trail",
    "pine":"New Jersey Pinelands National Reserve",
    "jazz":"New Orleans Jazz National Historical Park",
    "neri":"New River Gorge National River",
    "nepe":"Nez Perce National Historical Park",
    "nifa":"Niagara Falls National Heritage Area",
    "nico":"Nicodemus National Historic Site",
    "nisi":"Ninety Six National Historic Site",
    "niob":"Niobrara National Scenic River",
    "noat":"Noatak National Preserve",
    "noca":"North Cascades National Park",
    "noco":"North Country National Scenic Trail",
    "obed":"Obed Wild & Scenic River",
    "ocmu":"Ocmulgee Mounds National Historical Park",
    "oire":"Oil Region National Heritage Area",
    "okci":"Oklahoma City National Memorial",
    "olsp":"Old Spanish National Historic Trail",
    "olym":"Olympic National Park",
    "oreg":"Oregon National Historic Trail",
    "orca":"Oregon Caves National Monument & Preserve",
    "orpi":"Organ Pipe Cactus National Monument",
    "ovvi":"Overmountain Victory National Historic Trail",
    "oxhi":"Oxon Cove  Park & Oxon Hill Farm ",
    "ozar":"Ozark National Scenic Riverways",
    "pais":"Padre Island National Seashore",
    "paal":"Palo Alto Battlefield National Historical Park",
    "para":"Parashant National Monument",
    "pagr":"Paterson Great Falls National Historical Park",
    "peri":"Pea Ridge National Military Park",
    "valr":"Pearl Harbor National Memorial",
    "peco":"Pecos National Historical Park",
    "paav":"Pennsylvania Avenue ",
    "pevi":"Perry's Victory & International Peace Memorial",
    "pete":"Petersburg National Battlefield",
    "pefo":"Petrified Forest National Park",
    "petr":"Petroglyph National Monument",
    "piro":"Pictured Rocks National Lakeshore",
    "pinn":"Pinnacles National Park",
    "pisp":"Pipe Spring National Monument",
    "pipe":"Pipestone National Monument",
    "pisc":"Piscataway Park",
    "pore":"Point Reyes National Seashore",
    "poex":"Pony Express National Historic Trail",
    "poch":"Port Chicago Naval Magazine National Memorial",
    "pohe":"Potomac Heritage National Scenic Trail",
    "popo":"Poverty Point National Monument",
    "wicl":"President William Jefferson Clinton Birthplace Home National Historic Site",
    "whho":"President's Park (White House) ",
    "prsf":"Presidio of San Francisco ",
    "prwi":"Prince William Forest Park",
    "puho":"Pu`uhonua O Hōnaunau National Historical Park",
    "puhe":"Pu`ukoholā Heiau National Historic Site",
    "pull":"Pullman National Monument",
    "rabr":"Rainbow Bridge National Monument",
    "reer":"Reconstruction Era National Historical Park",
    "redw":"Redwood National and State Parks",
    "rich":"Richmond National Battlefield Park",
    "rigr":"Rio Grande Wild & Scenic River",
    "rira":"River Raisin National Battlefield Park",
    "rist":"Rivers Of Steel National Heritage Area",
    "rocr":"Rock Creek Park",
    "romo":"Rocky Mountain National Park",
    "rowi":"Roger Williams National Memorial",
    "roca":"Roosevelt Campobello International Park",
    "rori":"Rosie the Riveter WWII Home Front National Historical Park",
    "ruca":"Russell Cave National Monument",
    "sahi":"Sagamore Hill National Historic Site",
    "sagu":"Saguaro National Park",
    "sacn":"Saint Croix National Scenic Riverway",
    "sacr":"Saint Croix Island International Historic Site",
    "sapa":"Saint Paul's Church National Historic Site",
    "saga":"Saint-Gaudens National Historical Park",
    "stge":"Sainte Geneviève National Historical Park",
    "sama":"Salem Maritime National Historic Site",
    "sapu":"Salinas Pueblo Missions National Monument",
    "sari":"Salt River Bay National Historical Park and Ecological Preserve",
    "saan":"San Antonio Missions National Historical Park",
    "safr":"San Francisco Maritime National Historical Park",
    "saju":"San Juan National Historic Site",
    "sajh":"San Juan Island National Historical Park",
    "sand":"Sand Creek Massacre National Historic Site",
    "safe":"Santa Fe National Historic Trail",
    "samo":"Santa Monica Mountains National Recreation Area",
    "sara":"Saratoga National Historical Park",
    "sair":"Saugus Iron Works National Historic Site",
    "scrv":"Schuylkill River Valley National Heritage Area",
    "scbl":"Scotts Bluff National Monument",
    "semo":"Selma To Montgomery National Historic Trail",
    "seki":"Sequoia & Kings Canyon National Parks",
    "shen":"Shenandoah National Park",
    "shil":"Shiloh National Military Park",
    "sitk":"Sitka National Historical Park",
    "slbe":"Sleeping Bear Dunes National Lakeshore",
    "soca":"South Carolina National Heritage Corridor",
    "spar":"Springfield Armory National Historic Site",
    "stsp":"Star-Spangled Banner National Historic Trail",
    "stli":"Statue Of Liberty National Monument",
    "stea":"Steamtown National Historic Site",
    "stri":"Stones River National Battlefield",
    "sucr":"Sunset Crater Volcano National Monument",
    "tapr":"Tallgrass Prairie National Preserve",
    "tecw":"Tennessee Civil War National Heritage Area",
    "thko":"Thaddeus Kosciuszko National Memorial",
    "qush":"The Last Green Valley National Heritage Corridor",
    "thro":"Theodore Roosevelt National Park",
    "thrb":"Theodore Roosevelt Birthplace National Historic Site",
    "thri":"Theodore Roosevelt Inaugural National Historic Site",
    "this":"Theodore Roosevelt Island ",
    "thco":"Thomas Cole National Historic Site",
    "edis":"Thomas Edison National Historical Park",
    "thje":"Thomas Jefferson Memorial ",
    "thst":"Thomas Stone National Historic Site",
    "tica":"Timpanogos Cave National Monument",
    "timu":"Timucuan Ecological & Historic Preserve",
    "tont":"Tonto National Monument",
    "tosy":"Touro Synagogue National Historic Site",
    "trte":"Trail Of Tears National Historic Trail",
    "tule":"Tule Lake National Monument",
    "tuma":"Tumacácori National Historical Park",
    "tupe":"Tupelo National Battlefield",
    "tuai":"Tuskegee Airmen National Historic Site",
    "tuin":"Tuskegee Institute National Historic Site",
    "tuzi":"Tuzigoot National Monument",
    "ulsg":"Ulysses S Grant National Historic Site",
    "upde":"Upper Delaware Scenic & Recreational River",
    "vall":"Valles Caldera National Preserve",
    "vafo":"Valley Forge National Historical Park",
    "vama":"Vanderbilt Mansion National Historic Site",
    "vick":"Vicksburg National Military Park",
    "vive":"Vietnam Veterans Memorial",
    "viis":"Virgin Islands National Park",
    "vicr":"Virgin Islands Coral Reef National Monument",
    "voya":"Voyageurs National Park",
    "waco":"Waco Mammoth National Monument",
    "waca":"Walnut Canyon National Monument",
    "wapa":"War In The Pacific National Historical Park",
    "wamo":"Washington Monument ",
    "waro":"Washington-Rochambeau Revolutionary Route National Historic Trail",
    "waba":"Washita Battlefield National Historic Site",
    "wefa":"Weir Farm National Historic Site",
    "whee":"Wheeling National Heritage Area",
    "whis":"Whiskeytown National Recreation Area",
    "whsa":"White Sands National Park",
    "whmi":"Whitman Mission National Historic Site",
    "wiho":"William Howard Taft National Historic Site",
    "wicr":"Wilson's Creek National Battlefield",
    "wica":"Wind Cave National Park",
    "wing":"Wing Luke Museum Affiliated Area",
    "wotr":"Wolf Trap National Park for the Performing Arts ",
    "wori":"Women's Rights National Historical Park",
    "wwii":"World War II Memorial ",
    "wrst":"Wrangell - St Elias National Park & Preserve",
    "wrbr":"Wright Brothers National Memorial",
    "wupa":"Wupatki National Monument",
    "yell":"Yellowstone National Park",
    "york":"Yorktown Battlefield Part of Colonial National Historical Park",
    "yose":"Yosemite National Park",
    "yuho":"Yucca House National Monument",
    "yuch":"Yukon - Charley Rivers National Preserve",
    "zion":"Zion National Park"
}
```

The Nu"mber of pages total:

```html
<ul class="Pagination"><li class="prev active"><a href="#" aria-disabled="true" class="carrot-start">Previous <span class="visuallyhidden">page</span></a></li><li class="active"><a href="#" aria-disabled="true"><span class="visuallyhidden">You're currently on page</span>1</a></li><li><a href="#" class="page_number" data-page="2">2</a></li><li><a href="#" class="page_number" data-page="3">3</a></li><li><a href="#" class="page_number" data-page="4">4</a></li><li><a href="#" class="page_number" data-page="5">5</a></li><li><a href="#" class="page_number" data-page="6">6</a></li><li><a href="#" class="page_number" data-page="7">7</a></li><li class="gap">…</li><li><a href="#" class="page_number" data-page="48">48</a></li><li class="next"><a href="#" class="carrot-end">Next <span class="visuallyhidden">page</span></a></li></ul>
```


So the alerts are listed with titles of the park place:

```html
<div class="AggregatedAlerts__ParkHeading"><a href="/abli/planyourvisit/conditions.htm"><span class="park">Abraham Lincoln Birthplace National Historical Park</span></a><span class="state">Kentucky</span></div>
```