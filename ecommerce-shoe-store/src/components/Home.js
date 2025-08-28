import React, { useState } from 'react';

function Home({ addToCart }) {
  const [products] = useState([
    { id: 1, name: 'Shoe 1', price: '100', imageUrl: 'https://example.com/shoe1.jpg' },
    { id: 2, name: 'Shoe 2', price: '150', imageUrl: 'https://example.com/shoe2.jpg' },
    { id: 3, name: 'Shoe 3', price: '200', imageUrl: 'https://example.com/shoe3.jpg' },
    { id: 4, name: 'Shoe 4', price: '250', imageUrl: 'https://example.com/shoe4.jpg' }
  ]);

  return (
    <div className="product-listing">
      {products.map(product => (
        <div key={product.id} className="product">
          <img src={product.imageUrl} alt={product.name} className="product-image"/>
          <h2>{product.name}</h2>
          <p>${product.price}</p>
          <button onClick={() => addToCart(product)}>Add to Cart</button>
        </div>
      ))}
    </div>
  );
}

export default Home;