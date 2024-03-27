import React from "react"
import { useParams } from "react-router-dom"
import { useGetLocationQuery } from "../../features/api/apiSlice"
import { Chart, LineElement, BarElement, CategoryScale, LinearScale, PointElement, TimeScale } from "chart.js"
// import { Weather } from "../../features/weather/weatherSlice"
import { Line, Bar } from "react-chartjs-2"
import { ChartOptions,ChartData } from "chart.js"

Chart.register(
    LineElement,
    CategoryScale,
    LinearScale,
    PointElement,
    BarElement,
    TimeScale
    )
interface Weather {
      date: Date,
      name: string,
      temp: number,
      weather: string,
      snow: number,
      wind: number,
      rain: number,
      id: number,
    }
const WeatherItem: React.FC =() =>{{
    const { location } = useParams()
    const { data:loc, error, isLoading } = useGetLocationQuery(location)
    console.log(loc)

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

    const options: ChartOptions<'line'>= {
      scales: {
        x: {
          type: 'category',
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
            <Bar data={data}   />

        </>
    )
}}

export default WeatherItem
