/**
  <li
              class="list-group-item d-flex justify-content-between align-items-center"
            >
              <button class="delete-todo btn-sm btn-danger" data-id="">
                X
              </button>
 */

const ul = $("#cupcake-list");

async function getCupcakes() {
  let resp = await axios.get("/api/cupcakes");

  return resp;
}

let data = getCupcakes().then(data => console.log(data.data));

// console.log(data);
