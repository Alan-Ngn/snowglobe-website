export interface Weather {
    date: Date,
    name: string,
    temp: number,
    weather: string,
    snow: number,
    wind: number,
    rain: number,
  }

export interface WeatherState {
    weathers: any[]
  }
