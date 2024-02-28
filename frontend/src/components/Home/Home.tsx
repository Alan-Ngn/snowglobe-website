import React from "react"
import { useGetWeathersQuery } from "../../features/api/apiSlice"

const Home: React.FC = () => {
    const { data:weathers, error, isLoading } = useGetWeathersQuery({});
    // console.log(weathers[0])
    // console.log(weathers[0])
    return (
        <>
            <div>hi</div>
            {weathers && weathers.length > 0 && (
                <div>{weathers[0].name}</div>
            )}
        </>
    );
}
export default Home
