import PropTypes from 'prop-types';

function Cart({ cart = [] }) {
  // Helper to normalize price values
  const normalizePrice = (price) => {
    if (typeof price === 'number') return price;
    const cleanedPrice = price.replace(/[^\d.-]+/g, '');
    return parseFloat(cleanedPrice) || 0;
  };

  // Calculate the total price of items in the cart
  const totalPrice = cart.reduce((acc, curr) => acc + normalizePrice(curr.price), 0);

  // Currency formatter
  const formatCurrency = (amount) => {
    return new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(amount);
  };

  // Render cart items or empty state
  const renderCartItems = () => {
    if (cart.length === 0) {
      return <div aria-live="polite">Your cart is empty</div>;
    }
    return cart.map((item, index) => (
      <div key={item.id || `${item.name}-${index}`} className="cart-item">
        {item.imageUrl && <img src={item.imageUrl} alt={item.name || "Cart item"} className="cart-item-image" />}
        <div className="cart-item-details">
          <h3>{item.name}</h3>
          <p>{formatCurrency(normalizePrice(item.price))}</p>
        </div>
      </div>
    ));
  };

  return (
    <div className="cart-container">
      <h2>Your Cart</h2>
      <div className="cart-items">
        {renderCartItems()}
      </div>
      {cart.length > 0 && (
        <div className="cart-total">
          <strong>Total Price: {formatCurrency(totalPrice)}</strong>
        </div>
      )}
    </div>
  );
}

Cart.propTypes = {
  cart: PropTypes.arrayOf(PropTypes.shape({
    id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]),
    name: PropTypes.string.isRequired,
    price: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    imageUrl: PropTypes.string,
  }))
};

export default Cart;