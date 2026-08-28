import { Link } from "react-router-dom";

function Home() {
  return (
    <div className="page home">
      <h1>Welcome to MyStore</h1>
      <p>Discover our collection of high-quality products.</p>
      <Link to="/products" className="button">
        View Products
      </Link>
    </div>
  );
}

export default Home;
