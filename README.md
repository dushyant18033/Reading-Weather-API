# Reading-Weather-API
An easily interface-able API to extract weather details from a JSON-based weather API without using the JSON library.

a1.py contains some basic functions to read a JSON string and extract relevant details
a1.py also contains a function to pass a valid location along with an API key to return a JSON string read from ' http://api.openweathermap.org/data/2.5/forecast?q=<location>&APPID=<your API key> '

You would need a API key to access the web service. To get your
own API key, visit http://openweathermap.org/appid and sign up to get the
API key. For a good response, use a key once in 10 minute.
