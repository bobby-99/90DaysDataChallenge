let inventory = [];

function findProductIndex(name) {
    return inventory.findIndex(product => {
        return product.name === name.toLowerCase()
    });
}


function addProduct(product) {
    product.name = product.name.toLowerCase()
    for (let each of inventory) {
        if (each?.name === product.name) {
            each.quantity += product.quantity
            console.log(`${product.name} quantity updated`)
            return;
        }
    }
    inventory.push(product)
    console.log(`${product.name} added to inventory`)
}

// function removeProduct(product, quantity){
//   let remProduct;
//   let copy;
//   for (let prod of inventory){
//     if(prod?.name === product.toLowerCase()){
//       copy = {...prod}
//       remProduct = prod;
//       break;
//     }
//   }
//   if(!remProduct){
//     console.log(`${product.toLowerCase()} not found`)
//     return;
//   }
//   remProduct.quantity -= quantity
//   if(remProduct.quantity < 0){
//     console.log(`Not enough ${copy.name} available, remaining pieces: ${copy.quantity}`)
//     return;
//   } else if (remProduct.quantity === 0){
//       const index = inventory.findIndex(p => p.name === copy.name)
//       if (index !== -1) {
//         inventory.splice(index, 1);
//       }
//     } else {
//       console.log(`Remaining ${remProduct.name} pieces: ${remProduct.quantity}`)
//     }
//   }

function removeProduct(name, quantity) {
    const index = findProductIndex(name)
    if (index === -1) {
        console.log(`${name.toLowerCase()} not found`);
        return;
    }

    const product = inventory[index]
    if (product.quantity < quantity) {
        console.log(`Not enough ${product.name} available, remaining pieces: ${product.quantity}`)
        return;
    }
    product.quantity -= quantity;
    if (product.quantity === 0) {
        inventory.splice(index, 1)
    } else {
        console.log(`Remaining ${product.name} pieces: ${product.quantity}`)
    }
}


