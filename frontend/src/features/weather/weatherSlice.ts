import { createSlice, createAsyncThunk, PayloadAction } from "@reduxjs/toolkit";

export interface Weather {
    date: Date,
    name: string,
    temp: number,
    weather: string,
    snow: number,
    wind: number,
    rain: number,
    id: number,
  }
// Define the initial state
// interface WeatherState {
//     weathers: Weather[];
//     loading: 'idle' | 'pending' | 'succeeded' | 'failed';
//     error: string | null;
//   }

  // const initialState: WeatherState = {
  //   weathers: [],
  //   loading: 'idle',
  //   error: null,
  // };

  // Create an async thunk for fetching weather data
  // export const fetchWeatherData = createAsyncThunk('weather/fetchWeatherData', async () => {
  //   try {
  //     const response = await fetch('/api/weathers/');
  //     if (!response.ok) {
  //       throw new Error('Failed to fetch weather data');
  //     }
  //     const data = await response.json();
  //     return data;
  //   } catch (error: unknown) {
  //     if (error instanceof Error) {
  //       throw new Error(`An error occurred while fetching weather data: ${error.message}`);
  //     } else {
  //       throw new Error(`An unknown error occurred while fetching weather data`);
  //     }
  //   }
  // });

  // Create a slice using createSlice
  // const weatherSlice = createSlice({
  //   name: 'weather',
  //   initialState,
  //   reducers: {
  //     // Other synchronous actions can go here
  //   },
  //   extraReducers: (builder) => {
  //     builder
  //       .addCase(fetchWeatherData.pending, (state) => {
  //         state.loading = 'pending';
  //         state.error = null;
  //       })
  //       .addCase(fetchWeatherData.fulfilled, (state, action: PayloadAction<Weather[]>) => {
  //         state.loading = 'succeeded';
  //         state.weathers = action.payload;
  //       })
  //       .addCase(fetchWeatherData.rejected, (state, action) => {
  //           // Ensure the payload is of the expected type (string | undefined)
  //           state.loading = 'failed';
  //           state.error = (action.payload as string) || 'An unknown error occurred';
  //         });
  //   },
  // });

  // Export the reducer and actions
  // export const { reducer, actions } = weatherSlice;
