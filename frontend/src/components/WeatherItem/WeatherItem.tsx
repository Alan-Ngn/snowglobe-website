import React from "react"
import { useParams } from "react-router-dom"
import { useGetLocationQuery } from "../../features/api/apiSlice"
import { Chart, LineElement, CategoryScale, LinearScale, PointElement } from "chart.js"
import { Weather } from "../../features/weather/weatherSlice"
import { Line } from "react-chartjs-2"
import { ChartOptions,ChartData } from "chart.js"

Chart.register(
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement
    )
const WeatherItem: React.FC =() =>{{
    const { location } = useParams()
    const { data:loc, error, isLoading } = useGetLocationQuery(location)
    console.log(loc)
    // interface LineProps {
    //     options: ChartOptions<'line'>;
    //     data: ChartData<'line'>;
    //   }
    const data = {
        labels : loc?.map((row: Weather) => row.date) || [],
        datasets: [
            {
                label: 'Weekly Snow',
                data: loc?.map((row: Weather)=> row.snow) || [],
                fill: false,
                borderColor: 'rgb(75, 192, 192)',
                tension: 0.1,
            }
        ]

    }
    // const options: ChartOptions = {
    //     plugins: {
    //         // legend: true

    //     }, scales: {
    //         y: {

    //         }
    //     }
    // };
    const options: ChartOptions<'line'>= {
        scales: {
          x: {
            type: 'category', // Now 'category' scale should work without errors
            position: 'bottom',
          },
          y: {
            type: 'linear',
            beginAtZero: true,
          },
        },
      }
    return (
        <>
            <div>{location}</div>
            <Line data={data} options={options}  />

        </>
    )
}}

export default WeatherItem
