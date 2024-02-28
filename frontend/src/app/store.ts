import { configureStore } from "@reduxjs/toolkit";
import { apiWeatherSlice } from "../features/api/apiSlice";


// export interface RootState {
//     weather: WeatherState,
// }

export const store =  configureStore({
    reducer: {
        [apiWeatherSlice.reducerPath]: apiWeatherSlice.reducer
    },
    middleware: getDefaultMiddleware =>
        getDefaultMiddleware().concat(apiWeatherSlice.middleware),
})
// const store = configureStore({
//     reducer: {
//         weather: weatherReducer
//     }
// })

// export default store
// store.dispatch(fetchWeatherData());
