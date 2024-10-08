import { useEffect, useState } from 'react';
import ReactOpenApiRenderer from "@tx-dts/react-openapi-renderer";

function APIPanel()
{
    const [spec, setSpec] = useState(null);

    const fetchSpec = async () =>
    {
        await fetch('http://localhost:8000/openapi.json')
        .then(response => response.json())
        .then(data => setSpec(data));
    };

    useEffect(() =>
    {
        fetchSpec();
    }, []);

    return (
        <div id="api-content-container" className="page">
            {spec ? (
                <div>
                    <link
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"
                        rel="stylesheet"
                        integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6"
                        crossorigin="anonymous"
                    />

                    <ReactOpenApiRenderer specification={spec} />
                </div>
            ):
            (
                <p>Loading OpenAPI specification...</p>
            )}
        </div>
    );
}

export default APIPanel;
