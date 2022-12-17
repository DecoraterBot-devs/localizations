# localizations

This repository is for localizing all of DecoraterBot to a specific language.

## Adding a localization

To add a localization copy ``StringTable.en.sql`` to ``StringTable.<localization>.sql`` and then start translating.

Beware of all of the holes in the strings (the holes are text between ``{`` and ``}``) as those should not be translated.

After that submit a pull request to: https://github.com/DecoraterBot-devs/localizations/pulls

## Updating the localizations database.

The database itself lives in https://github.com/DecoraterBot-devs/DecoraterBot/ and is made in sqlite3.
To update it, you must first load the database into an editor (or an interactive python session) 
and run the new sql file to insert the new values into the database.
After that is done submit the updated database to: https://github.com/DecoraterBot-devs/DecoraterBot/pulls

After the update to the database is merged (after reviewing it manually), it should then eventually make it's way into the
official instance of the bot (they update *should* be able to be applied without restarting the bot).
