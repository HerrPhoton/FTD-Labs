function ConclusionPanel()
{
    return (
        <div id="conclusion-content-container" className="page">

            <h1 className="title" id="main-title">Пересекающиеся части в аудиозаписях музыкальных произведений</h1>

            <div id="conclusion-container">

                <h2 className="title" id="conclusion-title">Заключение</h2>

                <div id="conclusion-text-container" className="text-container">

                    <p>
                        <span>
                            В ходе работы был реализован прототип программного комплекса с нейросетевым алгоритмом, который способен выявлять
                            пересекающиеся части в аудиозаписях музыкальных произведений.
                        </span>
                    </p>

                    <p>
                        <span>
                            Результат был очень хороший, мне понравилось.
                        </span>
                    </p>

                </div>

            </div>

            <div id="metrics-container">

                <h2 className="title" id="metrics-title">Метрики</h2><br/>

                    <table id="metrics-table">

                        <tr>
                            <th>Название Метрики</th>
                            <th>Значение</th>
                        </tr>

                        <tr>
                            <td>Метрика 1</td>
                            <td>Отличная</td>
                        </tr>

                        <tr>
                            <td>Метрика 2</td>
                            <td>Неплохая</td>
                        </tr>

                    </table>

            </div>

        </div>
    );
}

export default ConclusionPanel;
