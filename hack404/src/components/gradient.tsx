const Gradient = () => {
    return (
        <div className="grid grid-cols-5 h-10 w-full rounded-lg mb-4">
            <div className="w-full h-full bg-[#B8E2DC] animate-bounce delay-5" />
            <div className="w-full h-full bg-[#B8E2D4] animate-bounce delay-10" />
            <div className="w-full h-full bg-[#B8E2CD] animate-bounce delay-15" />
            <div className="w-full h-full bg-[#B8E2C6] animate-bounce delay-20" />
            <div className="w-full h-full bg-[#B8E2B9] animate-bounce delay-25" />
        </div>
    )
}

export default Gradient;