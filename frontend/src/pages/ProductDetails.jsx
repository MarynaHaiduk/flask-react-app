import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { getProduct } from "../api";

function ProductDetails() {
  const { id } = useParams();
  const [product, setProduct] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function loadProduct() {
      try {
        const data = await getProduct(id);
        setProduct(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    loadProduct();
  }, [id]);

  if (loading) {
    return <p>Loading product...</p>;
  }

  if (error) {
    return (
      <div className="page">
        <h1>Product Not Found</h1>
        <p>{error}</p>
        <Link to="/products" className="button">
          Back to Products
        </Link>
      </div>
    );
  }

  return (
    <div className="page product-details">
      <h1>{product.name}</h1>
      <div className="product-details-card">
        <h2>{product.name}</h2>
        <p>{product.description}</p>
        <p className="price">${product.price.toFixed(2)}</p>
        <Link to="/products" className="button">
          ← Back to Products
        </Link>
      </div>
    </div>
  );
}

export default ProductDetails;
