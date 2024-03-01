import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const apiWeatherSlice = createApi({
    reducerPath: 'api',
    baseQuery:fetchBaseQuery({baseUrl: '/api'}),
    endpoints: builder => ({
        getWeathers: builder.query({
            query: () =>'/weathers'
        }),
        getLocation: builder.query({
            query: location => `/weathers/${location}`
        })
    })
})

export const { useGetWeathersQuery, useGetLocationQuery } = apiWeatherSlice
