# Contributing Better Translations

### Preamble

I am a native English speaker, and I don't know any other languages, so by necessity all the localization I have done in this project has been machine translation using Google Translate.

I'm sure it is awful, and I apologize for that.

My priorities while localizing the mod were:

- I wanted to be consistent with the names of objects and areas within the game, so I tried to match them as closely as possible to the offical From Software translations within the game files, even though it's clear that *those* aren't always good either.  
- For area names I needed to invent, I tried to ensure that each one was lexically distinct from all the others.  
- The hint object texts were constructed with the simplest connecting phrases and particles I could figure out to express the basic ideas of *this* object in *this* direction from *this* location. I did not have the knowledge to account for tense, gender, and so on.  

But if you are multilingual and would like to improve these translations, please feel free to do so and make a pull request. I'm pretty busy so I can't say how quickly I will be able to respond and review, but they are welcome.

Hopefully these instructions will make it easier for you make changes.

## Structure

All the files used for localization are in *source.data.locale*, and *source.model.locale.hintText*. Generally their file names are of the form "<*module name*\>_<*language code*\>.py", where the language codes are the ones From Software used in the game files.

The language codes are:  

- engus: English  
- deude: German  
- frafr: French  
- itait: Italian  
- jpnjp: Japanese  
- korkr: Korean  
- polpl: Polish  
- porbr: Brazilian Portugese  
- rusru: Russian  
- spaar: Latin American Spanish  
- spaes: European Spanish  
- thath: Thai  
- zhocn: Simplified Chinese  
- zhotw: Traditional Chinese  

#### *source.data.locale.itemInfo*

*itemInfo* contains a dictionary of every object in the game, using the in-game From Software translations as the keys. These keys are used in the user interface of Randomizer Hints to allow selection of items in the appropriate language.

Generally, there should be no need to change any of these keys since players will be most familiar with these names from their text within the game. However, I have changed a few of them because in some languages there were a couple identical names. You may be able to improve on this.

The values in this dictionary should not be changed.

#### *source.data.locale.localeData*

*localeData* is a simple dictionary hash consisting of English strings as keys and their equivalent localized strings as values. It is used to generally translate text for both the user interface and the in game hints.

The keys in this dictionary should not be changed, but you may add new entries with new keys based on your needs.

Most of the values up to the comment starting with "# ---" are translations mined directly from From Software's in game data and should probably not be changed, but all the values after that are machine translated and probably need improvement.

If you want to change the localized area and fog gate values I strongly suggest you check anything you do change against the other values to make sure you don't end up creating any duplicates.

That said, there are duplicate values for different English keys that refer to the same area. This is because the English area names for Item and Enemy Randomizer and Fog Gate Randomizer needed to be different for hint length and consistency. The important thing to note is that different logical areas should not have the same localized name to avoid ambiguous hints.

#### *source.data.locale.missableLots*

*missableLots* is a dictionary of item lot keys and localized spoiler descriptions used in the Missable Items tab in the user interface.

The keys in this dictionary should be not be changed, but the localized string values almost certainly need better translations.

#### *source.data.locale.uiText*

*uiText* is a dictionary of English string keys and localized string values used in the user interface of the program.

The keys in this dictionary should not be changed, but the localized string values almost certainly need better translations.

#### *source.data.locale.bellOfReturnText.py*

*bellOfReturnText* is a dictionary of localized string data for the Bell of Return item from Fog Gate Randomizer. Fog Gate Randomizer does not provide localized versions of the bell's name and description, so they are provided here, keyed by language code and XML file key.

The keys in this dictionary and its subdictionaries should not be changed, but the localized string values almost certainly need better translations.

#### *source.data.locale.hintText*

This folder is for any data files you wish to create to help with your localization in the *hintText* module. Please keep any data files you create inside the folder named after the language code of the language you are working with.

#### *source.model.locale.hintText*

*hintText* is the Python module that generates the localized strings needed to construct an in game hint, including the hint name, hint description, and the body of the hint.

Each localized *hintText* module is called with a dictionary of English *components* that will be used to construct a hint object, as well as the *localeData* for the language.

A *localize()* method is provided for easy localization of English components using *localeData*.

You'll want to construct your strings from these localized components using clear grammar, and you can use randomized variations if you wish.

The following two methods are used to construct the hint object names and descriptions from the *components* passed to *hintText*, and you should alter them to construct your localized versions.

#### *hintObjectName()*

>This method operates directly on the *components* argument passed to *hintText()*.  
>
>These components are:  
>
> - "hintName": If this key is present, its value should be directly localized to become the complete hint name, and the following components should be disregarded.  
> - "ownerName": The name of the person who owned the hint object.  
> - "ownerAdjective": An optional adjective describing the owner.  
> - "noteName": The name of the hint object.  
>
> The returned name should describe the note name and owner.

#### *hintObjectDescription(hintName)*

>This method operates directly on the *components* argument passed to *hintText*, as well as the passed *hintName* generated by *hintObjectName()* above.
>
>These components are:  
>
> - "hintDescription": If this key is present, its value should be directly localized to become the complete hint description, and the following components should be disregarded.  
> - "noteName": The name of the hint object.  
> - "noteAdjectives": A list of two unique adjectives that describe the hint object.  
>
> The returned description should begin with the "hintName", followed by appropriate punctuation, then the "noteName" modified by at least one or both of its "noteAdjectives"

The following method is used to construct a fog gate hint string from the components in a hint entry, and you should alter it to construct your localized versions.

#### *fogHint(hintEntry)*

> This method operates on the passed *hintEntry* dictionary which contains the following components:
>
> - "area": The game area the fog gate is in.
> - "destArea": The game area the fog gate leads to.
> - "gate": The name or description of the fog gate.
> - "pathAreas": An ordered list of game areas that are passed through on the way to the destination area.
>
> The returned hint should describe the gate and its location and where it leads to.

The *hintString()* method is used to construct a hint string from the components in a hint entry, and depending on which components are present, it calls one of the five following methods, which you should alter to construct your localized versions.

#### *randomDropHint(hintEntry)*

> This method operates on the passed *hintEntry* dictionary which contains the following components:
>
> - "chance": The likelihood of the enemy dropping the item.
> - "enemy": The name of the enemy that drops the item.
> - "item": The name of the item.
> - "quantity": The quantity of the item or "" if there is only 1.
>
> The method should return the localized hint describing how often the enemy drops the item.

#### *bookHint(hintEntry, isParent)*

> This method operates on the passed *hintEntry* dictionary which contains the following components:
>
> - "book": The name of the containing item.
> - "item": The name of the item.
> - "quantity": The quantity of the item or "" if there is only 1.
> - "parentEntry": The hint entry of the containing item.
>
> *hintString* should be called with the "parentEntry" and the *isParent* flag set to *True* to obtain a localized hint for the containing object.
>
> The returned hint should mention the item, it's containing item, and how to obtain the containing item, unless the *isParent* flag is set to *True*, in which case do not mention the item.

#### *npcHint(hintEntry, isParent)*

> This method operates on the passed *hintEntry* dictionary which contains the following components:
>
> - "foe": If this key is present, the name of the enemy that must be defeated for the NPC to offer the item.
> - "foeLocation": If this key is present, the name of the game area where the "foe" is.
> - "foeDirections": If this key is present, a dictionary of directional components that point to where the "foe" is.
> - "isShop": If this key is present, the item is in the shop inventory of the NPC.
> - "item": The name of the item.
> - "NPC": The name of the NPC that owns the item.
> - "npcLocation": The game area where the NPC resides, or "" if the NPC moves around.
> - "quantity": The quantity of the item or "" if there is only 1.
>
> If there is a "foe" quest:
> > Pass the "foeDirections" dictionary to *directionsString()* to get a localized directions string for the enemy.
> > When describing the "foe" quest you should randomly choose to use either the directions or the "foeLocation".
>
> The returned hint should mention the item, the NPC who owns or sells it, and the "foe" quest if there is one, unless the *isParent* flag is set to *True*, in which case do not mention the item.

#### *enemyHint(hintEntry, isParent)*

> This method operates on the passed *hintEntry* dictionary which contains the following components:
> 
> - "enemy": The name of the enemy that drops the item.
> - "directions": A dictionary of directional components that point to where the enemy is.
> - "item": The name of the item.
> - "quantity": The quantity of the item or "" if there is only 1.
>
> Pass the "directions" dictionary to *directionsString()* to get a localized directions string for the enemy.
>
> The returned hint should mention the item, the enemy that drops it, and the directions to the enemy, unless the *isParent* flag is set to *True*, in which case do not mention the item.

#### *treasureHint(hintEntry, isParent)*

> This method operates on the passed *hintEntry* dictionary which contains the following components:
>
> - "directions": A dictionary of directional components that point to where the item is.
> - "item": The name of the item.
> - "quantity": The quantity of the item or "" if there is only 1.
>
> Pass the "directions" dictionary to *directionsString()* to get a localized directions string for the item.
>
> The returned hint should mention the item and the directions to it, unless the *isParent* flag is set to *True*, in which case do not mention the item.

The following method is used to construct a directional description string, and you should alter it to construct your localized versions.

#### *directionsString(directions)*

> This method operates on the passed *directions* dictionary which contains the following components:
>
> - "angle": The compass direction relative to the landmark or "" if the distance is short.
> - "distance": Word(s) describing the distance relative to the landmark. Can be "" for intermediate distances.
> - "height": Word(s) that describe the altitude relative to the landmark. Can be "" if the altitude is about the same.
> - "landmark": An in game landmark or "" if there is no landmark.
> - "location": The game area the landmark is in.
>
> If there is no landmark, the returned directions string should only mention the location. Otherwise the returned distance string should mention the landmark and the location, and any directional information provided by "angle", "distance", and "height".

## Checking results

When you've generated hints with your new code, you can easily check the results by opening the XML files that are generated. In the main program folder go into *working/msg/<language code\>/item-msgbnd-dcx* and look for *GoodsCaption.fmg.xml*, *GoodsInfo.fmg.xml*, and *GoodsName.fmg.xml*. Depending on whether you use WitchyBND or Yabber, they may be right there or in a subfolder. Open the files with a text editor and your hints, names, and descriptions will appear starting at *text id="300000"*.

## Documentation translations

Just like the localizations in the program and the game, the README and Instructions files in the [docs](docs) folder are also badly machine translated. Improvements to those are welcome too.

# Other pull requests

Bugs or problems in the program are best handled with the Issues tracker, but if you submit a PR, I'll probably at least look it over.

If you have an exported settings file (.rhe) with settings you think make for a fun playthrough, I'm open to including it, but I may not be able to test it in a timely fashion.

I don't really intend at this time to expand the scope of this mod or add more features to it, although if you've got a reasonable feature idea I could be open to it.

If you want to make very significant changes, for instance adapting it to work with one of the large popular mod packages like Unalloyed, feel free to fork the project.