import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './components/Home';
import Cart from './components/Cart';

function App() {
  const [cart, setCart] = useState([]);

  const addToCart = useCallback((product) => {
    setCart((prevCart) => [...prevCart, product]);
  }, []);

  return (
    <Router>
      <div>
        <Switch>
          <Route exact path='/' render={() => <Home addToCart={addToCart} />} />
          <Route path='/cart' render={() => <Cart cart={cart} />} />
        </Switch>
      </div>
    </Router>
  );
}

export default App;