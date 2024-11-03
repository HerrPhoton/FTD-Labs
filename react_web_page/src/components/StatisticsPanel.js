import { useEffect, useState } from 'react';

function StatisticsPanel()
{
    const [spec, setSpec] = useState(null);

    const fetchSpec = async () =>
    {
        await fetch('http://localhost:8080/pages/kpi')
        .then(response => response.json())
        .then(data => setSpec(data));
    };

    useEffect(() =>
    {
        fetchSpec();
    }, []);

    return (
        <div id="statistics-content-container" className="page">
            {spec ? (
                <table className="kpi-table">
                    <tr>
                        <th>ID</th>
                        <th>Название страницы</th>
                        <th>Количество посещений</th>
                        <th>Общее время, с</th>
                    </tr>

                    {spec.data.map((page) =>
                    (
                        <tr key={page.id}>
                            <td>{page.id}</td>
                            <td>{page.name}</td>
                            <td>{page.visits}</td>
                            <td>{page.time}</td>
                        </tr>
                    ))}

                </table>
            ) : (
                <p>Загрузка статистики...</p>
            )}

        </div>
    );
}

export default StatisticsPanel;
