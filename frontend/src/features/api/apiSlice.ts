import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'

export const apiWeatherSlice = createApi({
    reducerPath: 'api',
    baseQuery:fetchBaseQuery({baseUrl: '/api'}),
    endpoints: builder => ({
        getWeathers: builder.query({
            query: () =>'/weathers'
        })
    })
})

export const { useGetWeathersQuery } = apiWeatherSlice
