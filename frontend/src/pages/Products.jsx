import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { getProducts } from "../api";

function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadProducts() {
      try {
        const data = await getProducts();
        setProducts(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    loadProducts();
  }, []);

  if (loading) {
    return <p>Loading products...</p>;
  }

  if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div className="page">
      <h1>Products</h1>
      <div className="products">
        {products.map((product) => (
          <div className="product-card" key={product.id}>
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <strong>${product.price.toFixed(2)}</strong><br />
            <Link to={`/products/${product.id}`} className="button">
              View Details
            </Link>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Products;
