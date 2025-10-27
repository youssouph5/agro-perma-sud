import { useEffect, useState } from 'react'
import { motion, useInView } from 'framer-motion'
import { useRef } from 'react'

interface Stat {
  label: string
  value: number
  suffix?: string
  icon?: React.ReactNode
}

interface StatsCounterProps {
  stats: Stat[]
}

const StatsCounter = ({ stats }: StatsCounterProps) => {
  const ref = useRef(null)
  const isInView = useInView(ref, { once: true })

  return (
    <section ref={ref} className="section bg-primary-50">
      <div className="container-custom">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {stats.map((stat, index) => (
            <StatCard key={index} stat={stat} isInView={isInView} delay={index * 0.1} />
          ))}
        </div>
      </div>
    </section>
  )
}

const StatCard = ({ stat, isInView, delay }: { stat: Stat; isInView: boolean; delay: number }) => {
  const [count, setCount] = useState(0)

  useEffect(() => {
    if (isInView) {
      let start = 0
      const end = stat.value
      const duration = 2000
      const increment = end / (duration / 16)

      const timer = setInterval(() => {
        start += increment
        if (start >= end) {
          setCount(end)
          clearInterval(timer)
        } else {
          setCount(Math.floor(start))
        }
      }, 16)

      return () => clearInterval(timer)
    }
  }, [isInView, stat.value])

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.5, delay }}
      className="text-center"
    >
      {stat.icon && (
        <div className="flex justify-center mb-4 text-primary-500">
          {stat.icon}
        </div>
      )}
      <div className="text-4xl md:text-5xl font-bold text-primary-700 mb-2">
        {count}
        {stat.suffix}
      </div>
      <div className="text-lg text-gray-700">{stat.label}</div>
    </motion.div>
  )
}

export default StatsCounter
