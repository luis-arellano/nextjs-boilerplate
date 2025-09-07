export default function Hero() {
  return (
    <section className="flex flex-col items-center justify-center min-h-screen px-4 text-center">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl md:text-6xl font-bold mb-6 text-foreground">
        Boilerplate Next.js 15
        </h1>
        <p className="text-lg md:text-xl mb-8 text-foreground/80 max-w-2xl mx-auto leading-relaxed">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod 
          tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim 
          veniam, quis nostrud exercitation ullamco laboris.
        </p>
        <div className="flex flex-col sm:flex-row gap-4 justify-center">
          <button className="px-8 py-3 bg-foreground text-background rounded-lg font-medium hover:opacity-90 transition-opacity">
            Get Started
          </button>
          <button className="px-8 py-3 border border-foreground/20 text-foreground rounded-lg font-medium hover:bg-foreground/5 transition-colors">
            Learn More
          </button>
        </div>
      </div>
    </section>
  );
}
