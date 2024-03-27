use reqwest::Client;

fn main() {

    // Define the URL you want to fetch HTML from
    let url: &str = "https://chaturbate.com/aalliyahh";
    let res = test(url);
    println!("{:?}", res);

}

#[tokio::main]
async fn test(url: &str) -> Result<(), Box<dyn std::error::Error>> {
    // Create a new reqwest Client
    let client = Client::new();

    // Make a GET request to the URL
    let response = client.get(url).send().await?;

    // Check if the request was successful (status code 200 OK)
    if response.status().is_success() {
        // Get the HTML body as a string
        let html = response.text().await?;
        println!("HTML from {}: {}", url, html);
    } else {
        println!("Failed to fetch HTML from {}", url);
    }

    Ok(())
}

