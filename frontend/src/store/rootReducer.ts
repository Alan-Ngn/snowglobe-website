import { combineReducers } from "@reduxjs/toolkit";
import weatherReducer from "../reducers/weatherReducer";
import { WeatherState } from "../types/weatherTypes";

export interface RootState {
    weather: WeatherState,
}

const rootReducer = combineReducers({
    weather: weatherReducer
})

export default rootReducer
