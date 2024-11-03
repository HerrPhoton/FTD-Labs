import { useEffect, useState } from 'react';
import SwaggerUI from 'swagger-ui-react';
import { usePageTracking } from '../hooks/usePageTracking';
import root from 'react-shadow';

function APIPanel() 
{
    usePageTracking('api');
    
    const [spec, setSpec] = useState(null);

    const fetchSpec = async () => 
    {
        await fetch('http://localhost:8080/openapi.json')
        .then(response => response.json())
        .then(data => setSpec(data));
    };

    useEffect(() => 
    {
        fetchSpec();
    }, []);

    return (
        <div id="api-content-container" className={spec ? "api" : "page"}>
            {spec ? (
                <root.div style={{backgroundColor: 'white'}}>
                    <link rel="stylesheet" href="https://unpkg.com/swagger-ui-react/swagger-ui.css" />
                    <SwaggerUI
                        spec={spec}
                        url={null}
                        docExpansion="list"
                        supportedSubmitMethods={['get', 'post', 'put', 'delete']}
                    />
                </root.div>
            ) : (
                <p>Загрузка спецификации OpenAPI...</p>
            )}
        </div>
    );
}

export default APIPanel;
