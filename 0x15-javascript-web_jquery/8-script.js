$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (const key in data.results) {
    const film = $('<li></li>').text(data.results[key].title);
    $('#list_movies').append(film);
  }
});
