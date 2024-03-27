import React from "react"
import { useGetWeathersQuery } from "../../features/api/apiSlice"
import { Link } from "react-router-dom";
// import { Weather } from "../../features/weather/weatherSlice";
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
const WeatherList: React.FC = () => {
    const { data:weathers, error, isLoading } = useGetWeathersQuery({});
    // console.log(weathers[0])
    console.log(weathers)
    return (
        <>
            <div>hi</div>
            {weathers && weathers.length > 0 && (
                weathers.map((weather: Weather)=> (
                    <Link to={`/${weather.name}`}>
                        <div>{weather.name}</div>

                    </Link>
                ))
            )}
        </>
    );
}
export default WeatherList
