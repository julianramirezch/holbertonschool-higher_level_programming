$('#add_item').on('click', function () {
  const item1 = $('<li></li>').text('Item');
  $('.my_list').append(item1);
});
