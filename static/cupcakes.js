const ul = $("#cupcake-list");

async function getCupcakes() {
  /*Append cupcakes in db to ul */
  let resp = await axios.get("/api/cupcakes");
  let cupcakesArray = resp.data.cupcakes;
  //   console.log(cupcakesArray);
  cupcakesArray.forEach(cupcake => {
    flavor = cupcake.flavor.charAt(0).toUpperCase() + cupcake.flavor.slice(1);
    ul.append(
      `<li class="list-group-item d-flex align-items-center"><img src="${cupcake.image}" alt="${flavor} cupcake image" class="cupcake-image">
      ${flavor}</li>`
    );
  });
}

$("#add-btn").on("click", addCupcake);

async function addCupcake(e) {
  new_cupcake = {
    flavor: $("#flavor").val(),
    size: $("#size").val(),
    rating: $("#rating").val(),
    image: $("#image").val(),
  };
  await axios.post("/api/cupcakes", {
    flavor: $("#flavor").val(),
    size: $("#size").val(),
    rating: $("#rating").val(),
    image: $("#image").val(),
  });
  e.preventDefault();
}

getCupcakes();

/*
Add later
// Rating: ${cupcake.rating}
// <button class="delete-todo btn-sm btn-danger" data-id="${cupcake.id}">X</button>

*/
