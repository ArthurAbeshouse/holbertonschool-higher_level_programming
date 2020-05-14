$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const feature of data.results) {
    $('UL#list_movies').append('<li>' + feature.title + '</li>');
  }
});
