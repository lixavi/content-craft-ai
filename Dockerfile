# Use the official .NET SDK as the base image
FROM mcr.microsoft.com/dotnet/sdk:3.1 AS build-env

# Set the working directory inside the container
WORKDIR /app

# Copy the project file and restore dependencies
COPY *.csproj ./
RUN dotnet restore

# Copy the remaining source code and build the application
COPY . ./
RUN dotnet publish -c Release -o out

# Create the final runtime image
FROM mcr.microsoft.com/dotnet/aspnet:3.1
WORKDIR /app
COPY --from=build-env /app/out .

# Expose the port on which the application will listen
EXPOSE 80

# Define the command to run the application when the container starts
ENTRYPOINT ["dotnet", "Hypnose.dll"]
