import { usePageTracking } from '../hooks/usePageTracking';

function DescriptionPanel()
{
    usePageTracking('description');
    
    return (
        <div id="description-content-container" className="page">

            <h1 className="title" id="main-title">Пересекающиеся части в аудиозаписях музыкальных произведений</h1>

            <div id="description-container">

                <h2 className="title" id="description-title">Описание</h2>

                <div id="description-text-container" className="text-container">

                    <p>
                        <span>
                            Входные аудиозаписи переводятся в спектрограмму.
                            Затем нейросетевой алгоритм обрабатывает данные изображения для выявления пересекающихся частей.
                        </span>
                    </p>

                </div>
            </div>

            <div id="example-container">

                <h2 className="title" id="example-title">Пример</h2><br/>

                <div id="image-container">
                    <img src="spectr.png" alt="example" id="example-image"/><br/>
                    <span id="example-image-label">Рис. 1. Пример поиска пересекающихся частей по двум входных аудиозаписях</span>
                </div>

            </div>

            <div id="params-container">

                <h2 className="title" id="params-title">Параметры</h2><br/>

                    <table id="params-table">

                        <tr>
                            <th>Название Параметра</th>
                            <th>Описание</th>
                            <th>Диапазон значений</th>
                        </tr>

                        <tr>
                            <td>Порог чувствительности</td>
                            <td>Определяет восприимчивость системы к похожим частям</td>
                            <td>0 - 1.0</td>
                        </tr>

                        <tr>
                            <td>Размер окна</td>
                            <td>Определяет длину отрывка аудиофайлов для поиска пересечений</td>
                            <td>0 - 1.0</td>
                        </tr>

                        <tr>
                            <td>Параметр</td>
                            <td>Описание</td>
                            <td>Значения</td>
                        </tr>

                    </table>

            </div>

            <div id="application-container">

                <h2 className="title" id="application-title">Область применения</h2>

                <ul>
                    <li>Отслеживание плагиата на медиа-платформах</li>
                    <li>Поиск полной аудиозаписи по отрывку</li>
                </ul>

            </div>

        </div>
    );
}

export default DescriptionPanel;
